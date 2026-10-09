# T2 homepage resources — partial read-only audit, 2026-10-09

Status: BLOCKED for exact historical 22 failures. No production resources/code/settings changed; GA4/Clarity untouched.

Homepage HTTP200 and self canonical, index/follow. HTML extraction found 58 unique directly referenced JS/CSS/image/font URLs; list stored in home-static-resource-urls-2026-10-09.json. First 12 HEAD checks stored in home-resource-sample-2026-10-09.json. This is a limited server-side HTTP sample, not a browser network trace and not the historical Googlebot 78-resource inventory. CSS imports, lazy load, scripts and browser policy may add resources. HTTP success does not establish CORS/JavaScript/render success; HEAD failure may not equal GET failure.

GSC 22/78 is repository historical count, not current identified failure URLs. Do not claim resources repaired or count cleared. Need URL Inspection -> crawled page -> failed resources list with URLs/reasons/time (22), or browser HAR plus Google crawl list for reconciliation. Browser control sandbox failure previously verified today; no repeated login request. Production fix proposals require WAITING_APPROVAL and exact affected references/backups.
