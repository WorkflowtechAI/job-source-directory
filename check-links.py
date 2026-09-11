#!/usr/bin/env python3
"""Re-check every link in README.md and report what came back.

usage:
    python3 check-links.py            # write status.json
    python3 check-links.py --dry-run  # check and print, write nothing

No dependencies beyond the standard library.

IT FAILS CLOSED. If fewer than MIN_OK_RATIO of links come back healthy it
assumes this machine lost network rather than that the web died, refuses to
write, and exits non-zero. Publishing "all 113 sources are dead" because a
laptop dropped its wifi is worse than publishing nothing.

Three false positives it deliberately does not report, all found the hard way:

  * A 403 is bot protection, not a dead site. Several of these boards serve a
    browser and refuse a default user agent. We send a browser UA and record
    403, 405, 406 and 429 as "blocked", which counts as healthy.
  * A www redirect is not a move. Nine of these links bounce between www and the
    bare domain. Hostnames are compared with www stripped and the port ignored.
  * A failed HEAD is not a dead site, and HEAD never gets the final word here.
    Measured 2026-09-11: elempleo answered HEAD with 500 and GET with 200;
    usemassive answered HEAD with 400 and GET with 200. Both load fine in a
    browser. Only GET decides, and only 404 and 410 mean gone.

A fourth it cannot fix: reachability depends on where you ask from. At least one
entry returns 200 from a US host and does not resolve at all elsewhere. If you
report a dead link, say which country you checked from.
"""

from __future__ import annotations

import json
import os
import re
import ssl
import sys
import tempfile
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "README.md")
OUT = os.path.join(HERE, "status.json")

TIMEOUT = 20
RETRIES = 2
PAUSE = 0.4
MIN_OK_RATIO = 0.70

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/140.0.0.0 Safari/537.36")

# Repo-internal links and anything that is not a directory entry.
SKIP_HOSTS = {"github.com", "www.github.com"}

MD_LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")


def collect_links(path: str) -> list[str]:
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    seen: set[str] = set()
    out: list[str] = []
    for url in MD_LINK.findall(text):
        url = url.rstrip(".,;")
        host = (urlparse(url).hostname or "").lower()
        if host in SKIP_HOSTS or url in seen:
            continue
        seen.add(url)
        out.append(url)
    return out


def same_site(a: str, b: str) -> bool:
    """Same site if the hostnames match once www is stripped and port ignored."""
    def host(u: str) -> str:
        name = (urlparse(u).hostname or "").lower()
        return name[4:] if name.startswith("www.") else name

    return host(a) == host(b)


def probe(url: str) -> dict:
    """Return a verdict for one URL. Never raises."""
    ctx = ssl.create_default_context()
    last_error = ""
    for attempt in range(RETRIES + 1):
        for method in ("HEAD", "GET"):
            request = urllib.request.Request(
                url, method=method,
                headers={"User-Agent": UA, "Accept": "*/*"})
            try:
                with urllib.request.urlopen(request, timeout=TIMEOUT,
                                            context=ctx) as response:
                    final = response.geturl()
                    moved = not same_site(final, url)
                    return {"url": url,
                            "state": "moved" if moved else "ok",
                            "code": response.status,
                            "final_url": final if moved else ""}
            except urllib.error.HTTPError as exc:
                if method == "HEAD":
                    continue  # HEAD is advisory only; let GET decide
                if exc.code in (404, 410):
                    return {"url": url, "state": "dead", "code": exc.code,
                            "final_url": ""}
                if exc.code in (403, 405, 406, 429):
                    return {"url": url, "state": "blocked", "code": exc.code,
                            "final_url": ""}
                return {"url": url, "state": "error", "code": exc.code,
                        "final_url": ""}
            except Exception as exc:  # noqa: BLE001
                last_error = type(exc).__name__
        if attempt < RETRIES:
            time.sleep(PAUSE * (attempt + 1))
    return {"url": url, "state": "unreachable", "code": 0, "final_url": "",
            "error": last_error}


def main() -> int:
    dry_run = "--dry-run" in sys.argv

    if not os.path.exists(PAGE):
        print(f"check-links: no README.md at {PAGE}", file=sys.stderr)
        return 2

    links = collect_links(PAGE)
    if not links:
        print("check-links: found no links, refusing to write", file=sys.stderr)
        return 2

    results = []
    for url in links:
        results.append(probe(url))
        time.sleep(PAUSE)

    healthy = [r for r in results if r["state"] in ("ok", "blocked")]
    problems = [r for r in results if r["state"] not in ("ok", "blocked")]
    ratio = len(healthy) / len(results)

    print(f"check-links: {len(results)} links, {len(healthy)} healthy "
          f"({ratio:.0%}), {len(problems)} to look at")
    for r in problems:
        arrow = f"  ->  {r['final_url']}" if r.get("final_url") else ""
        print(f"  {r['state']:<12} {r['code'] or '-':>4}  {r['url']}{arrow}")

    if ratio < MIN_OK_RATIO:
        print(f"check-links: only {ratio:.0%} healthy, below the "
              f"{MIN_OK_RATIO:.0%} floor. That looks like a problem with this "
              f"machine, not with the web. Refusing to write status.json.",
              file=sys.stderr)
        return 1

    payload = {
        "note": ("Written by check-links.py. A 'blocked' link is bot "
                 "protection, not a dead site. See the README."),
        "checked_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "checked_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total": len(results),
        "healthy": len(healthy),
        "problems": problems,
    }

    if dry_run:
        print("check-links: --dry-run, nothing written")
        return 0

    handle, temp_path = tempfile.mkstemp(dir=os.path.dirname(OUT), suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2)
            fh.write("\n")
        os.replace(temp_path, OUT)
    except Exception:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise

    print(f"check-links: wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
