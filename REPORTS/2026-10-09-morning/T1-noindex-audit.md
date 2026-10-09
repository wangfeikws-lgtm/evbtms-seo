# T1 noindex — partial read-only audit, 2026-10-09

Status: BLOCKED for complete 22-URL acceptance. No production change. Remote main b2fc375 fetched and fast-forwarded before work; reused existing task definitions.

GSC count 22 is historical repository evidence (Oct 8 / data Oct 4), not an exported URL list. Current first-party HTTP evidence in read-only-evidence-2026-10-09.json: homepage, three collection pages and two yesterday articles all HTTP200, meta robots follow/index, self canonical, no X-Robots-Tag exclusion observed. These six checks do NOT establish the identity or cause of the historical 22 exclusions. Sitemap/indexability is not proof of actual Google indexing.

Cannot responsibly recommend removing noindex without actual excluded URLs and page purpose. Intentional admin/search/duplicate archives must remain excluded. Runtime HTML identifies directives but not necessarily plugin/global/template source.

Minimum input: GSC Pages -> excluded by noindex -> URL list export (22 real URLs, snapshot date). Then compare each live meta/header, page purpose and authenticated plugin/page settings. No password needed in chat. Exact plugin/global/source attribution remains pending. Any proposed production noindex change must be WAITING_APPROVAL; nothing changed or submitted to Google.
