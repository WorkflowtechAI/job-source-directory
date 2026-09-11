---
name: Dead or changed source
about: A listed source no longer resolves, moved, shut down, or now sells something else
title: "[dead] "
labels: correction
---

**Which entry**

Name and URL as they appear in the README.

**What you saw**

Did it fail to resolve, redirect somewhere unrelated, shut down, get acquired, or quietly change what it sells?

**How you checked**

Browser or script, and roughly when.

**Which country you checked from**

Genuinely useful. At least one entry returns 200 from a US host and does not resolve at all elsewhere, so reachability is a property of where you asked.

---

**Before you file, please rule these out.** Each one makes a healthy site look broken:

- [ ] I opened it in a real browser, not just a script. A **403 is usually bot protection**, not a dead site.
- [ ] It is not just a **`www` versus bare domain** redirect. Nine entries here do that normally.
- [ ] I did not judge it on a **failed HEAD request**. Some of these hosts answer HEAD with 500 or 400 and serve the same URL fine on GET.
