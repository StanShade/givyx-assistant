# Backend audit — raw findings (2026-07-18)

Auth is opt-in per endpoint (no global RequireAuthorization). Any endpoint missing
.AddPortalAuthorization()/.AddAccessFilter() is ANONYMOUS.
Payments (Stripe Connect + platform subs), plans/gating, forms, analytics, MCP — all BUILT
(payments well-tested; NOT "mid-build"). Fixed: Kestrel dual-stack, MCP timeout/cancellation,
table-storage escaping (partial), upsert_tenant_plan Stripe-id wipe.

## OPEN findings
1. **P0 security M — /apps and /apps/{appId} CRUD COMPLETELY UNAUTHENTICATED (AppsApi.cs).**
   GET /apps lists every tenant; POST/PUT/DELETE open. DELETE cascades LocationTeardownService
   (wipes user grants + all per-location stores) then deletes app row. Anyone on internet can
   enumerate all tenants + hard-delete a paying client's app + data. MUST close before paying clients.
2. P1 security M — App-scoped reads check only "valid token" not ownership. GET /apps/{appId}/plan =
   any authed user reads any app tier; GET /apps/{appId}/locations/{locationId} has NO auth (anonymous
   read of location incl. email). The deferred "B2 auth gap" — broader than noted (some routes anonymous).
3. P1 security S — JWTs effectively non-expiring (RequireExpirationTime=false, no ValidateLifetime).
   MCP tokens = TokenType=Auth, 365-day → accepted on portal-auth-only endpoints. Leaked token never expires.
4. P1 reliability M — Stripe webhooks have NO event-id idempotency/dedupe. Replays can double-insert
   orders / double-apply refunds (Stripe is at-least-once).
5. P1 bug M — Analytics summary undercounts clicks/submits for ranges >6mo old (rollup branch hardcodes
   page_view). KPI tiles vs chart disagree. Bites ~Dec 2026.
6. P1 reliability M — 32K Table ceiling: over-limit page/manifest write fails opaquely, MCP reports
   SUCCESS. No pre-write size guard. Silent content loss (2 /services edits dropped).
7. P1 security S — Public form submissions have honeypot-only spam protection, NO rate limit (limiter
   exists but only on analytics/inquiries). Each submit also emails tenant → DB flood + inbox spam.
8. P1 reliability M — Fire-and-forget notifications: no delivery monitoring/retry; NotifyEmails defaults
   empty → silent non-delivery. Workshop can silently miss customer leads. SendGrid only.
9. P2 missing-feature L — No SMS channel anywhere (PortalUsersService.cs:123 "TODO send login sms"). Email only.
10. P2 tech-debt S — TableRepository runs sync CreateTableIfNotExists in ctor per request.
11. P2 bug S — RowKey.Split("_") breaks if pageId contains underscore (WebPagesRepository.cs:57).
12. P2 tech-debt M — RedisBus.QueryAsync throws NotImplementedException (cross-instance query gap).
13. P2 data-model M — seo.title/description not localizable (string?), seo.locales dropped API-side.
14. P2 data-model M — Contact/form field labels can't be localized (plain-string). Non-EN visitors see English form.
15. P2 tech-debt S — Dead ctas analytics breakdown still queried API-side (safe to remove now).
16. P2 improve S — PlanService parses SPONSORED_APP_IDS env per request (make singleton).
17. P2 security S — Analytics ingest trusts left-most XFF (spoofable → rate-limit bypass).

## Summary
Backend is functionally broad + mature (payments well-tested). The BLOCKING gap is AUTHORIZATION:
/apps CRUD incl. data-destroying cascade DELETE is fully anonymous (#1); app-scoped ownership missing
across /apps/{appId}/* (#2). Must close before any paying client. Second tier: non-expiring/over-scoped
tokens (#3), webhook idempotency (#4), analytics undercount (#5), silent >32K loss (#6), unthrottled
form spam + unmonitored lead notifications (#7/#8).
