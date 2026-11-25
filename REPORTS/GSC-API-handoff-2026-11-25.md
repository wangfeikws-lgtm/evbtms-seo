# EVLINK Search Console API handoff · 2026-11-25

- Asset: https://evbtms.com/ (URL-prefix property).
- Route: Google Cloud CLI operator OAuth on Peter's computer → IAM Credentials short-lived impersonation → Search Console Search Analytics API. The service account has Restricted access on this GSC property. Scope is webmasters.readonly. No service-account keys, OAuth credentials, or tokens are included.
- Verified: final web search property totals, top queries and pages for 7 and 28 days, and query × page dimensions (68-keyword evidence in today's CSV). Whole-property index coverage totals were not verified through the API. Keep the current coverage-report source for that figure.
- Handoff choice: A. Codex produces the snapshots from the authorized machine and Muse reads repository files. First snapshot accompanies this handoff. The daily 08:20 target requires a run on the authorized machine. This submission does not enable a recurring job.
- Latest finalized day with data: 2026-11-22. 7 days: 3 clicks, 688 impressions, 0.44% CTR, position 24.63. 28 days: 20 clicks, 1,946 impressions, 1.03% CTR, position 28.22. Window dates follow Search Console reporting.
- Auth storage: isolated local CLI config in the temporary directory. It must survive or be reauthorized for later runs. Muse does not need the operator's credentials.
