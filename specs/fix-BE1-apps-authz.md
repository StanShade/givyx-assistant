# Fix plan — BE-1: lock down the /apps API (authorization)

**Severity:** P0 security · **Repo:** Givyx.Api · **For:** executor agent in givyx.claudeBrain (read its CLAUDE.md).
**Status:** PLAN — needs Stan's approval to implement (backend + prod-affecting).

## Problem
`Givyx.Api/Api/Application/AppsApi.cs` — the `/apps` route group has NO `AddPortalAuthorization()` and no
access/ownership filter. So `GET /apps` (lists every tenant), `GET /apps/{appId}`, `POST /apps`,
`PUT /apps/{appId}`, and `DELETE /apps/{appId}` are anonymous. The DELETE cascades
`LocationTeardownService.TeardownAsync` across every location (wipes user grants + all per-location
stores) then deletes the app row. **Anyone on the internet can enumerate all tenants and hard-delete a
paying client's app and data.**

## CRITICAL backward-compat constraint (read first)
The shared API serves live tenant sites. Some of these endpoints may be called anonymously by the
**websites renderer** (givyx.websites) to render `*.givyx.com` / custom-domain sites, and by the
**Portal** (authenticated) and **MCP**. **Do NOT add auth blindly — you will break live sites.**

**Step 0 (mandatory): enumerate every caller** of each `/apps` and `/apps/{appId}` route before changing it:
- grep givyx.websites for `/apps` fetches (e.g. utils/location-context.ts, proxy.ts, any api client).
- grep Givyx.Portal utils/api.ts for `/apps` calls.
- check Givyx.Mcp tools for `/apps` calls.
- confirm how the renderer resolves a tenant (it uses `GET /locations/by-domain/{domain}` per the ops
  audit — verify whether it ALSO hits `/apps/{appId}` anonymously during render).
Write the caller map into `Givyx/findings/` before editing.

## Fix — two phases (ship Phase 1 now; Phase 2 carefully)

### Phase 1 — lock all MUTATIONS (urgent, low risk)
`POST /apps`, `PUT /apps/{appId}`, `DELETE /apps/{appId}` must require auth + app-ownership.
- Mirror the pattern already used by `PaymentsApi.cs` (which correctly opts routes into
  `.AddPortalAuthorization()` + `.AddAccessFilter(...)`). Use the same DI'd services.
- Ownership: the AccessFilter keys off a `{locationId}` route value, which `/apps/{appId}` routes don't
  have. So add/borrow an **app-ownership check**: resolve the caller's `UserId` from the JWT and verify
  membership on `appId` (there is a membership/teardown model — `LocationTeardownService`, PortalUsers/
  PortalAdmin APIs reference grants). If no app-level membership lookup exists, add one
  (`AccessService.ValidateAppAccessAsync(appId, userId, requiredRole)`), following the existing
  `ValidateAccessAsync(locationId, userId, role)` shape.
- DELETE specifically: require the highest role (Owner/PlatformAdmin). Never anonymous.
- Mutations are NOT on the render hot path, so locking them cannot break live sites. This alone closes
  the "anyone can delete a tenant" hole.

### Phase 2 — tighten READS (careful, after the caller map)
`GET /apps`, `GET /apps/{appId}`:
- `GET /apps` (lists ALL apps) must become admin-only or user-scoped to the caller's apps.
- `GET /apps/{appId}`: if the renderer needs app data anonymously to render, do NOT simply block it —
  instead (a) return only the minimal public fields needed for rendering via a dedicated public shape,
  and (b) gate the full/admin fields behind ownership. If the renderer does NOT use it, require ownership.
- Also fix the sibling leak noted in BE-2: `GET /apps/{appId}/locations/{id}` currently anonymous
  (leaks `location.Email`) — same treatment (public-minimal vs owner-full). Track BE-2 as a fast-follow.

## Acceptance criteria
- Anonymous `POST/PUT/DELETE /apps*` → 401/403 (verified with a token-less request).
- A portal user who does NOT own `appId` → 403 on mutations of that app.
- The owner (and PlatformAdmin) → still succeeds.
- **All live sites still render** (givyx.com, ipr.givyx.com, a slug tenant, the intracars preview) — smoke
  each after the change (this is the backward-compat gate from the brain CLAUDE.md §3).
- Existing Portal flows (create/edit app, locations) still work for authenticated owners.

## Verification
- New/updated xUnit tests: anonymous mutation → rejected; non-owner → 403; owner → 200; DELETE requires
  Owner/PlatformAdmin. `dotnet build` + full test run clean.
- MCP/Portal smoke of the app CRUD an owner actually uses.
- Smoke the 4 live sites for render regressions.

## Risk / rollback
- Risk = breaking an anonymous render dependency (Phase 2). Phase 1 (mutations) is near-zero risk.
- Land Phase 1 first, verify live sites, then do Phase 2 behind the caller map. Standard branch→verify→
  land-on-main flow; watch the deploy green.
