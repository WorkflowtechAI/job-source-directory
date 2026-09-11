# Contributing

The directory is only worth something because the entries were opened rather than copied. That decays. Corrections keep it alive and are more valuable than additions.

## Reporting a dead or changed source

The highest-value contribution. Open an issue or a PR and say what you actually saw:

- The URL
- What happened: it does not resolve, it redirects somewhere unrelated, it shut down, it was acquired, it now sells something else
- How you checked, and roughly when

**Before reporting a link as dead, rule out the three false positives.** Each one makes a healthy site look broken:

1. **A 403 is bot protection, not death.** Several of these boards serve a browser fine and refuse anything that looks scripted. Open it in a real browser before concluding anything.
2. **A `www` redirect is not a move.** Nine of these links bounce between `www.` and the bare domain.
3. **A failed HEAD means nothing.** Some of these hosts answer HEAD with a 500 or a 400 and serve the identical URL fine on GET.

And a fourth: **reachability depends on where you ask from.** At least one entry returns 200 from a US host and does not resolve at all from some other countries. If a link fails for you, saying which country you checked from is genuinely useful information.

## Adding a source

A new row needs three things:

| Field | What it needs |
|---|---|
| **Site** | The name people use, linked to the page a job seeker should actually land on. Not a marketing homepage if a listings page exists. |
| **What it is** | One or two plain sentences. What it carries, who it is for, and any gate. No marketing language. |
| **Feed or API** | `Yes` plus the endpoint if there is a free keyless machine-readable path. Otherwise `No`, or name the gate: `Paid`, `Affiliate-gated`, `Manual approval`. |

Put it in the section it belongs to. If you are unsure which, open an issue instead of guessing.

**Say how you verified it.** A PR that says "I opened this and saw Solutions Engineer roles in LATAM" is worth ten that say "adding X, it is good."

## What gets rejected

- **Affiliate links, referral codes and tracking parameters.** Strip them. A directory that can be paid into is exactly what this one exists to be an alternative to.
- **Sources that charge job seekers to view or apply**, unless the row says so plainly in the description.
- **Marketing copy.** "The leading platform for ambitious professionals" tells a reader nothing. What does it carry, and what does it cost?
- **Bulk additions.** Ten rows in one PR with no evidence any of them were opened is the failure mode this directory exists to correct.
- **Software engineering job boards with no infrastructure, operations, security or customer-facing technical roles.** There are better lists for those.

## Style

- Plain sentences. No em dashes or en dashes anywhere.
- Say the unflattering thing when it is true. "Heavy staffing-agency reposts" and "nearly empty when checked" are why a reader trusts the rest of the row.
- Numbers only if you saw them on a page you fetched.

## Running the checker

```bash
python3 check-links.py --dry-run   # check and print, write nothing
python3 check-links.py             # write status.json
```

No dependencies beyond the Python 3 standard library. It fails closed: below 70% healthy it assumes your network is the problem and refuses to write a report.
