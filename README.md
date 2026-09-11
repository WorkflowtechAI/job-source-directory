# Job Source Directory

**113 job boards, aggregators and contracting platforms.**

Weighted toward information security, technology leadership, and customer-facing technical roles. The aggregator and remote sections are general.

Last verified **2026-09-11**. See [how this stays honest](#keeping-this-honest).

> **Corrections and additions are wanted.** Open a PR or an issue. A source that turned out to be dead, a description that has drifted, or a board that belongs here and is missing are all worth a minute of your time and will save someone else an afternoon. [How to contribute](CONTRIBUTING.md).

---

## How to read the Feed column

A source with a free, keyless, machine-readable path is worth more than a bigger name without one, because it can be polled on a schedule instead of browsed. Those are marked **Yes**, and they are the ones worth wiring into anything automated.

## If you check these links yourself, three false positives will bite you

All three were live while this was being built, and each one reports a perfectly healthy site as broken.

1. **A 403 is not a dead site.** Several of these boards serve a browser fine and refuse a default user agent. Send a browser user agent, and still treat 403, 405, 406 and 429 as *blocked*, never as *gone*.
2. **A `www` redirect is not a move.** Nine of the links below redirect between `www.` and the bare domain. Compare hostnames with `www.` stripped, or you will get nine false alarms on every pass.
3. **A failed HEAD is not a dead site.** Measured 2026-09-11: elempleo answered HEAD with 500 and GET with 200; usemassive answered HEAD with 400 and GET with 200. Both load perfectly in a browser. Let GET decide, and treat only 404 and 410 as gone.

And a fourth that no code can fix: **reachability is a property of where you ask from.** ExecuNet returns 200 from a US host and does not resolve at all from some other networks. A checker run from the wrong network reports healthy sites as dead.

There is a checker in this repo that respects all four: [`check-links.py`](check-links.py).

---
## Job aggregators


### General

| Site | What it is | Feed or API |
|---|---|---|
| [Dice](https://www.dice.com/jobs) | Best generalist for IT, infrastructure, security and contract work. Heavy staffing-agency reposts. | No |
| [LinkedIn Jobs](https://www.linkedin.com/jobs/search) | Highest raw density of any board. Recruiters are reachable directly. | No public API |
| [Indeed](https://www.indeed.com/jobs) | Largest single pool. Geo-redirects to a local edition based on your IP address. | Partner-gated |
| [Built In](https://builtin.com/jobs/cybersecurity-it) | Tech-focused with real cybersecurity and IT verticals, including director-level lines. | No |
| [SimplyHired](https://www.simplyhired.com/search) | Good density of IAM, endpoint, SecOps and GRC titles. No login to browse. | No |
| [Glassdoor](https://www.glassdoor.com/Job/index.htm) | Volume, plus salary and review context. | No |
| [Talent.com](https://www.talent.com/) | Aggregator. Geo-redirects to a local edition based on your IP address. | No |
| [JobServe](https://www.jobserve.com/us/en/Job-Search/) | IT contract work, weighted to the UK. | No |
| [Jobgether](https://jobgether.com/remote-jobs) | Remote roles with genuine per-country filters. | No |
| [Wellfound](https://wellfound.com/jobs) | Startups. Formerly AngelList Talent. | No |
| [Welcome to the Jungle](https://www.welcometothejungle.com/en/jobs) | Absorbed Otta and retired that brand. Login-walled, skews startup software engineering. | No |
| [Adzuna](https://developer.adzuna.com/) | Aggregator with documented developer access. | Yes, free key |
| [The Muse](https://www.themuse.com/api/public/jobs?page=1&category=Computer%20and%20IT) | Curated employer profiles plus listings. | Yes, public |
| [jobdata API](https://jobdataapi.com/) | Aggregated ATS postings. Foorilla's own docs point here rather than at their paid tier. | Yes, anonymous |
| [Workable search](https://jobs.workable.com/) | Cross-employer search over every Workable-hosted board. | Yes, `/api/v1/jobs` |
| [Careerjet](https://www.careerjet.com/) | Aggregator. API exists but is for affiliates building job sites. | Affiliate-gated |
| [Jooble](https://jooble.org/) | Aggregator. API key issued by manual approval only. | Manual approval |
| [TheirStack](https://theirstack.com/en/job-posting-api) | Job-posting data product rather than a board. | Paid |
| [Fantastic.jobs](https://developer.fantastic.jobs) | Aggregates 54 ATS platforms. Redundant if you poll the ATS APIs yourself. | Paid, from $95/mo |


### Remote-focused

| Site | What it is | Feed or API |
|---|---|---|
| [Himalayas](https://himalayas.app/jobs) | Large remote index with real per-country pages. Cursor pagination, not offset. | Yes, `/jobs/api` + RSS |
| [Remotive](https://remotive.com/) | Carries eligibility as a structured field, so region is filterable rather than inferred. | Yes, `/api/remote-jobs` |
| [We Work Remotely](https://weworkremotely.com/) | Predatory and parasitic, but popular. Access for job-seekers is paywalled. | Yes, RSS per category |
| [RemoteOK](https://remoteok.com/) | Open feed, no account. Developer-first by construction, so filter hard. | Yes, `/api` |
| [Working Nomads](https://www.workingnomads.com/jobs) | Curated remote listings by category. | Yes, `/api/exposed_jobs/` |
| [Jobicy](https://jobicy.com/) | Remote board with a documented public feed. | Yes, `/api/v2/remote-jobs` |
| [Get on Board](https://www.getonbrd.com/jobs) | Latin America native. Listings in Santiago, Bogota, Lima, Mexico, Buenos Aires. | Yes, `/api/v0/search/jobs` |
| [Remote Rocketship](https://www.remoterocketship.com/) | Per-country and per-title filters. Listings render without paying. | No |
| [JustRemote](https://justremote.co/remote-jobs) | Remote board. | No |
| [Jobspresso](https://jobspresso.co) | Curated remote roles. | No |
| [Torre](https://torre.ai) | Latin America native, profile-driven matching. | No |


### Information security

| Site | What it is | Feed or API |
|---|---|---|
| [InfoSec Job Board](https://www.infosecjobboard.com/) | The strongest in this category. Breaks out Solutions Engineering, Customer Engineering and CISO as browsable departments, not just analyst roles. | Yes, keyless JSON + MCP |
| [CyberSecJobBoard](https://cybersecjobboard.com/) | Free, 24 or more security categories, actively maintained. Employer names are hidden on listing cards. | No |
| [ISACA Career Center](https://jobs.isaca.org/) | Skews to audit, GRC and academia rather than hands-on security operations. | No |
| [SANS Internet Storm Center](https://isc.sans.edu/jobs/) | Carried two live listings when checked. A bookmark, not a pipeline. | No |
| [foorilla](https://foorilla.com/hiring/infosec-privacy/) | Where isecjobs.com was consolidated. Its own docs point you at the free jobdata API instead of its paid tier. | Paid, $64/mo |
| [ClearanceJobs](https://www.clearancejobs.com/) | **Requires an active federal security clearance to register at all.** | No |
| [CyberSecJobs.com](https://cybersecjobs.com/) | Same clearance gate. Direct employers only, no staffing firms. | No |
| [CyberSecurityJobsite](https://www.cybersecurityjobsite.com/) | United Kingdom and Ireland only. | No |
| [CyberSN](https://cybersn.com/) | Specialist security staffing firm rather than a browsable board. | No |


### Technology leadership

The famous executive boards mostly start at VP and above and gate leads behind a fee. Several retained search firms publish no listings at all, only a resume form. The portfolio boards are the underrated entries here: they aggregate an entire investor's companies in one place.

| Site | What it is | Feed or API |
|---|---|---|
| [Forgepoint Capital](https://jobs.forgepointcap.com/jobs) | Cybersecurity-only venture portfolio board. | No |
| [Ten Eleven Ventures](https://jobs.1011vc.com/jobs) | Cybersecurity-only venture portfolio board, larger than Forgepoint. | No |
| [Insight Partners](https://jobs.insightpartners.com/jobs) | Private equity portfolio board covering security and infrastructure vendors. | No |
| [USAJOBS](https://www.usajobs.gov/) | United States federal hiring. Citizenship is the gate. | Yes, REST + RSS + export |
| [GovernmentJobs / NEOGOV](https://www.governmentjobs.com/) | State and local government. Real volume of actual IT Director titles. | No |
| [HigherEdJobs](https://www.higheredjobs.com/admin/search.cfm?JobCat=163) | Has a category named IT Manager and Director, which few boards do. | No |
| [EDUCAUSE](https://jobs.educause.edu/) | Higher education IT, CIO down to manager. | No |
| [SIM Career Center](https://careers.simnet.org/) | Society for Information Management. The peer network outweighs the listing volume. | No |
| [NTEN](https://www.nten.org/jobs/) | Nonprofit technology leadership. | No |
| [ExecThread](https://execthread.com/) | Crowdsourced confidential executive roles. Genuinely unposted inventory, membership-gated. | No |
| [Chief Jobs](https://www.chiefjobs.com/cio-jobs/) | CIO only, and nearly empty when checked. | No |
| [ExecuNet](https://www.execunet.com/) | Paid membership pitched at $200K and above. | No |
| [Ladders](https://www.theladders.com/) | Browsing is free, filtering and applying are not. | No |


### Pre-sales, managed services, and a regional cluster

The last three rows are Colombia's national job boards. They are here as a
worked example rather than because Colombia is special: almost every country has
two or three of these, they are invisible to anyone optimising for the US remote
market, and that is exactly why they are worth finding. Replace them with the
equivalents for wherever the search actually is.

| Site | What it is | Feed or API |
|---|---|---|
| [PreSales Collective](https://www.presalescollective.com/jobs) | The only board built around solutions and sales engineering. The [Slack](https://www.presalescollective.com/slack) carries a jobs channel. | No |
| [MSP Hire](https://msphire.com/jobs/) | Managed service provider roles specifically. | No |
| [Cloudtango](https://www.cloudtango.net/) | Directory of MSPs by country. A target list, not a board. | No |
| [r/msp](https://www.reddit.com/r/msp/) | Practitioner community. Hiring threads appear regularly. | No |
| [MSPGeek](https://mspgeek.org/) | Roughly 18,000 MSP practitioners across forums, Discord and Slack. No job board. | No |
| [HireLatam](https://hirelatam.com/jobs/) | Places Latin American candidates into United States remote roles. | No |
| [Hire With Near](https://www.hirewithnear.com/) | Same model, Latin America to United States remote. | No |
| [elempleo](https://www.elempleo.com/co/ofertas-empleo/) | Colombia national job board. | No |
| [Computrabajo](https://co.computrabajo.com/) | Colombia and wider Latin America. | No |
| [Magneto365](https://magneto365.com/co/empleos) | Colombia national job board. | No |


## AI-powered job search

What separates each site in the category below is who presses submit, and whether you are the customer or the inventory. Beware predators and data parasites who take your resume and then introduce a paywall.


### Search and matching

| Site | What it is | Price |
|---|---|---|
| [Jack & Jill](https://www.jackandjill.ai/) | Two paired agents. Jack works for you, Jill works for employers. A roughly ten-minute conversation, then daily scanning, and where Jill has employer coverage it makes a direct introduction to the hiring manager instead of an application. Value depends entirely on that employer network, not on the listing count. | Free to seekers |
| [HiringCafe](https://hiringcafe.com/) | Crawls company career pages directly and uses AI to parse each posting into structured facts: years required, named tools, salary, clearance, languages, travel. Every result links back to the employer's own posting. No account needed. | Free |
| [Jobright.ai](https://jobright.ai/) | Matching, per-posting resume tailoring, autofill across major ATS platforms, and referral contacts at target companies. Markets an agent that runs the search continuously. | Freemium, price not published |
| [Talentprise](https://www.talentprise.com/) | Profile-driven matching where recruiters pay per profile accessed rather than to post. | Free to seekers |
| [Levels.fyi Jobs](https://www.levels.fyi/jobs/) | Compensation-first search over a dataset built for comparing levels and pay bands. | Free to search |


### Application tools, where you still press submit

These autofill, tailor and track. None of them submits anything on your own account, so none carries the board-terms exposure of the group below.

| Site | What it is | Price |
|---|---|---|
| [Simplify](https://simplify.jobs/) | Browser extension that autofills applications on a very large number of company career sites from a saved profile, plus matching and a tracker. The same company runs a talent-agency business selling to employers, so your profile feeds that side too. | Freemium, price not published |
| [Teal](https://www.tealhq.com/) | Resume builder, tailoring and application tracker. The AI features sit behind the paid tier. | Freemium, from about $29 per 30 days |
| [Huntr](https://huntr.co/) | Application tracker with resume tailoring, keyword scanning against a job description, and an autofill extension. The free tier caps tailored resumes at two, which is the feature most people want it for. | Freemium, Pro $40/mo |
| [Careerflow](https://www.careerflow.ai/) | Resume and LinkedIn optimization, cover letters, autofill, tracking, mock interviews. Sources no listings of its own. | Freemium, from about $14/mo annually |
| [Jobscan](https://www.jobscan.co/) | Resume and ATS keyword matching against a specific posting. Auto Apply is sold separately as credits, one per application attempt. | Freemium, $49.95/mo or $29.98/mo quarterly |


### Auto-apply, where a third party submits for you

Read the risk column before the price column. Two things recur. The volume tiers sit far above the rate at which LinkedIn and Indeed start issuing CAPTCHAs and temporary activity blocks, and those submissions come from your logged-in session, so the account that gets restricted is yours. And several of these are not AI at all: Applyish and ApplyAll both describe human staff reviewing and submitting.

| Site | What it does | Price | Risk |
|---|---|---|---|
| [LazyApply](https://lazyapply.com/) | Submits on Greenhouse, Dice, Indeed and ZipRecruiter from inside your own browser session. | $99 to $999 per year | Top tiers offer 150 and 1,500 applications per day. Runs as you, from your account. |
| [JobCopilot](https://jobcopilot.com/) | Configurable copilots that filter, tailor and submit. | Quoted per day, about $28 to $32/mo | Per-day quoting hides the monthly figure until checkout. No refund policy published, no free tier to test match quality. |
| [LoopCV](https://www.loopcv.pro/) | Scans 30 or more boards daily and applies without per-role input. | Free tier, paid from about 10 euros/mo | Refunds only within 7 days and only if under 10% of the quota is used. Priced in euros. |
| [ApplyPass](https://www.applypass.com/) | Scrapes Greenhouse, Ashby, Workable, Workday and Glassdoor hourly and applies on company sites. | Free tier, $99 or $199/mo | The free tier deliberately delays you to listings already 7 days old, so the paywall is on freshness. Scoped to software engineering. |
| [Massive](https://usemassive.com/) | Matches, tailors and submits on autopilot, with visa filtering. | Not published anywhere public | Markets that employers cannot tell the application was automated. Terms state all payments are nonrefundable, on a subscription that auto-renews. |
| [AIApply](https://aiapply.co/) | A bundle of resume, cover letter and interview tools, with auto-apply sold separately as credit packs. | Not published anywhere public | The thing you are buying it for is not in the subscription. You pay for the plan, then again per application pack. |
| [Applyish](https://applyish.com/) | **People, not a bot.** Their own wording is that their team applies on your behalf. | $55 to $65/week, or $240/mo | No review step before your name goes on a submission. Weekly billing annualizes to roughly $2,860. |
| [ApplyAll](https://www.applyall.com/) | **Human-verified** rather than autonomous, sold as a one-time block rather than a subscription. | $249 or $299 one-time | Lowest risk in this group: no auto-renewal, no per-day volume. Confirm what starts the 30-day refund clock before paying. |


### AI-vetted marketplaces, and what is on the other side of the table

Most of this group has quietly become AI-training and model-evaluation gig work sold to AI labs, not the software staffing marketplaces they were famous for. That is paid project work, not employment, and it builds toward nothing in a technology leadership track. The last two are sold to recruiters, so a job seeker cannot join them at all.

| Site | What it is | Pay |
|---|---|---|
| [Mercor](https://www.mercor.com/experts/) | Contract work evaluating and improving AI models. An adaptive AI interview screens you in, then humans match you to projects. | Advertised $112/hr average, $60 to $250 band |
| [micro1](https://www.micro1.ai/experts) | AI-training projects screened by an AI interviewer, then a certification step. The corporate site now sells AI data infrastructure to labs rather than placing engineers. | No rate published at all |
| [Outlier](https://outlier.ai/) | Operated by Scale AI. Writing prompts, building grading rubrics, and rating model answers. | No rate published. Quality-scored |
| [Alignerr](https://www.alignerr.com/) | Powered by Labelbox. Prompt writing, evaluation, search quality, and AI red team testing. | Advertised $80/hr average, $40 to $120 band |
| [Handshake AI](https://joinhandshake.com/ai/) | A fellowship training and evaluating models. A separate division from the Handshake student job board. **Requires United States work authorization.** | About $40 to $125/hr, ceilings not rates |


## Contracting and freelance platforms

The split that matters here is whether a platform's work is hand-authored code. Several well-known networks are vetted developer benches and nothing else, which makes them a poor fit for infrastructure, operations or solutions consulting no matter how good their rates are.

| Site | What it carries | Gate |
|---|---|---|
| [Upwork](https://www.upwork.com/freelance-jobs/) | Everything. Highest volume, lowest signal. | Free login |
| [Braintrust](https://www.usebraintrust.com/jobs) | Has a real IT and Infrastructure category. Takes no fee from talent. Roughly nine in ten roles overall are software engineering. | Free login |
| [Toptal](https://www.toptal.com/project-managers) | The developer track is a live coding gauntlet. The project management track is a separate marketplace. | Approved profile |
| [Gun.io](https://gun.io) | Vetted developer bench. Payroll reach in 100 or more countries. | Approved profile |
| [Arc.dev](https://arc.dev) | Developers. | Approved profile |
| [A.Team](https://www.a.team/join) | Engineers, AI architects, product, and fractional CTOs. Acceptance under 2%. | Approved profile |
| [Turing](https://turing.com/jobs) | Developers and data scientists. Vetting includes a live technical interview. | Approved profile |
| [Andela](https://www.andela.com/) | Repositioned to AI application, data and platform engineering. | Approved profile |
| [Contra](https://contra.com) | Creative-dominated, with a smaller developer slice. Commission-free. | Free |
| [Catalant](https://catalant.com/for-independent-consultants/) | Strategy and operations consulting. Buyers are Fortune 1000 and private equity. | Free login |
| [Business Talent Group](https://www.businesstalentgroup.com/talent/) | Consulting engagements. Owned by Heidrick & Struggles. | Approved profile |
| [freelancermap](https://www.freelancermap.com/it-projects.html) | Categories are genuinely IT infrastructure, compliance and automation. Weighted to Europe. | Free |
| [Field Nation](https://fieldnation.com/) | On-site IT labour in the United States. The buyers are MSPs and service providers. | Free login |
| [Field Engineer](https://www.fieldengineer.com/) | On-site field engineering work. | Free login |
| [GLG](https://glg.com/for-experts) | Expert network. Paid hourly for domain knowledge, with no delivery work. | Approved profile |
| [Go Fractional](https://www.gofractional.com/jobs) | Fractional executive roles. Free, no login, and filters are addressable by URL. | Free |
| [Fractional Jobs](https://www.fractionaljobs.io/) | Fractional executive retainers. Mostly restricted to the United States. | Free |
| [TechCXO](https://www.techcxo.com/careers/) | Fractional CIO, CISO and CTO practice areas. | Interest form |
| [Bolster](https://bolster.com/) | Started as a self-serve fractional marketplace, has drifted to recruiter-led executive search. | Approved profile |
| [Cerius Executives](https://www.ceriusexecutives.com/) | Interim and fractional executives. | Approved profile |
| [InterimExecs](https://interimexecs.com/) | Interim executive placement. | Approved profile |
| [Connectd](https://www.connectd.com/) | Fractional and advisory, weighted to the United Kingdom. | Free login |
| [Outvise](https://outvise.com/) | Telecom and digital transformation consultants. | Approved profile |
| [Torc](https://www.torc.dev/) | Developer network owned by Randstad Digital. | Approved profile |
| [Bowman Williams](https://bowmanwilliams.com/all-jobs/) | Managed-services-exclusive staffing. Public board, no login, 93 pages deep. | Free |
| [TECLA](https://www.tecla.io/) | Nearshore Latin America. Places IT consultants and project managers, not only developers. | Free login |
| [Sagan Recruitment](https://saganrecruitment.com/career/) | Latin America into United States remote roles. | Free |
| [Support Adventure](https://supportadventure.com/remote-jobs/) | MSP service desk staffing. Hires worldwide with a short excluded-country list. | Free |

## What is deliberately not here

- **Anything gated behind an active security clearance.** ClearanceJobs and
  CyberSecJobs.com both require one to register at all, which makes them
  unusable for most readers rather than merely selective.
- **Retained executive search firms that publish no listings.** Several of the
  best-known names are a resume drop and a contact form. That is not a source
  you can work, and listing it as one wastes a reader's afternoon.
- **Dead sites.** Several widely recommended boards no longer exist, including
  one that shut down in June 2026 and one that was acquired and turned into a
  recruiting firm in 2023. They are not listed as "defunct" here because a
  directory is a list of places to go, not a graveyard. If a name you expected
  is missing, that is the likely reason.

---

## Keeping this honest

**Links get re-checked on a schedule.** [`check-links.py`](check-links.py) fetches every URL here and reports what it got. It respects the four traps above, and it **fails closed**: if fewer than 70% of links come back healthy it assumes the machine lost network rather than that the web died, and refuses to write a report claiming everything is dead.

```bash
python3 check-links.py --dry-run   # check and print, write nothing
python3 check-links.py             # write status.json
```

**Descriptions get re-checked by hand, less often.** Links outlive accuracy. A platform quietly changes what it sells while its URL keeps resolving, and no link checker will ever catch that. The entries most prone to it are the AI platforms and the talent marketplaces: several in the list above were remote developer staffing a year before this was written and are AI-training gig work now.

That second job is why pull requests matter more than the script does.

## Contributing

Corrections are more valuable than additions, and both are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Short version:

- **A dead or changed source** is the highest-value report. Say what you saw.
- **A new source** needs a link, one sentence on what it actually is, and whether it exposes a free feed.
- **No affiliate links, no referral codes, no SEO filler.** A source that pays to be listed is exactly what this directory exists to be an alternative to.

## Licence

[CC BY 4.0](LICENSE). Use it, republish it, build on it. Attribution appreciated, corrections more so.
