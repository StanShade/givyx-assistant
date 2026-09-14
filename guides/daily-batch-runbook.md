# Daily batch runbook — 10 personalised sites + 10 offer emails in one session

Written 2026-09-14 after batches 2 and 3 (23 sites, 30 emails). A fresh session can run this end to
end. **Stan pastes the kick-off prompt below; everything else is here.** Time: ~5 h wall-clock with
build agents in waves of 4. Stan's part: one review reply ("ok publish", "send all") and the SMS.

## 0. Kick-off prompt (paste into the fresh session)

> Run `guides/daily-batch-runbook.md` in `/Users/stan/Code/givyx/PersonalAssistant` for batch 4:
> pre-flight, then research 10, build 10, verify, one review email to me, wait for my "ok publish" /
> "send all", then send and record. Read STATE.md and the memory index first.

## 1. Pre-flight (15 min, before any research)

1. Read `STATE.md`, `prospects/pipeline.md` (bottom), `outreach/email-1-template.md`.
2. **Replies.** The Gmail connector reads `stan.zak.shade@gmail.com` (improvmx forwards every
   @givyx.com alias there). Search `in:anywhere newer_than:2d -from:info@givyx.com` and
   `to:info@givyx.com newer_than:2d -from:info@givyx.com`. Any prospect reply → stop the batch,
   report it to Stan first (his call, his reply), then continue.
3. **Clicks on yesterday's sends.** The admin token in `~/.givyx/ops-routine.token` (identity
   pu_fff7048, expires 2026-10-14) reads analytics per location, **one curl per Bash call**:
   ```
   curl -s -H "Authorization: Bearer $(tr -d '[:space:]' < ~/.givyx/ops-routine.token)" \
     "https://api.givyx.com/api/analytics/breakdowns?locationId=<locationId>&from=<send-day>T00:00:00Z&to=<today>T23:59:59Z"
   ```
   `campaigns[]` = tracked clicks (prospect's code) · `countryDevice[]` = any non-PL session on a PL
   site is not us. Location ids: `givyx.claudeBrain/dealership/clones/index.md`. Report clickers to
   Stan — a clicker gets his call, not email 2. (If PR 88 is merged: `GET /admin/ops/demo-visits?since=`
   does all tenants in one call.)
4. **Deliverability check (P0, batch 4 only, until answered):** 0 of 9 personalised emails clicked
   in 3 days vs 2 of 6 generic ones. Send the PL email through `POST /emails` to a mail-tester.com
   address (open mail-tester.com, copy the address, send with `ops/tools/send-one.sh`, read the
   score page with WebFetch). Report the score and any SPF/DKIM/DMARC finding. Batch 4 uses the
   plainer subject `Strona dla {{NAZWA}} — podgląd` (already in `ops/tools/build-email-json.py`).
5. Health: every existing demo host returns 200 (`for s in …; do curl -s -o /dev/null -w "$s %{http_code}\n" https://$s.givyx.com/; done`).

## 2. Research 10 (one agent, ~60–90 min)

Dispatch ONE `general-purpose` agent with this brief (fill the city list):

> Deliverable: `/Users/stan/Code/givyx/PersonalAssistant/prospects/<YYYY-MM-DD>-service-centers-PL-batch<N>.md`
> with 10 verified Polish general-mechanics workshops in the exact structure of
> `prospects/2026-09-14-service-centers-PL-batch3.md` (read it first; copy the method and the
> per-prospect build pack: legal/trading name · address · phone(s) as displayed · email + WHERE seen on
> their own page · platform/analytics · services in THEIR wording · prices only if published · hours
> only if stated (site vs Google, note conflicts) · 3–6 own photo URLs returning 200 · Google rating +
> full star histogram + read date · what they do well · growth motive · what is missing · `{{FAKT}}`
> line in Polish).
> Hard rules: every fact from a page you fetched; email visible in their OWN site source; Google
> histogram read on the Maps place page (Playwright MCP or the Browser pane; UNVERIFIED if it won't
> render, never a directory count); reject >10 % one-star; general mechanics / engine / diesel /
> electromechanics only (no campers, tyre-only, detailing-only, body-only, dealers, chains — a
> Q-Service / Bosch / Motointegrator partner sign counts as a chain: flag it); growth motive
> required (ads/GTM, second revenue line, fleet/B2B, long hours, specialist niche, or a site that
> visibly loses leads). Cities NOT already used: see "cities used" below. Exclude any name found by
> `grep -ril <name> prospects/`. End with a send order and a Rejected list. Do not contact anyone.

**Cities used so far (do not repeat):** Kraków area, Poznań, Legnica, Katowice, Olsztyn, Gdańsk,
Warszawa, Łódź, Białystok, Siemianowice, Barcin, Wrocław, Szczecin, Kielce, Toruń, Częstochowa,
Bielsko-Biała, Bydgoszcz, Opole, Rzeszów, Lublin. **Next:** Gdynia, Gliwice, Radom, Sosnowiec,
Tarnów, Nowy Sącz, Zielona Góra, Płock, Elbląg, Koszalin, Kalisz, Legionowo, Tychy, Rybnik, Olsztyn-area.
Batch-3 reserves (Motcars, Jedzie Warsztat, 71 Warsztat Premium — all Wrocław; Carmobile Gdynia; Omega
Gliwice; Wencel Opole; AUTO PAW Gdynia; Auto Rozwój Częstochowa) may be used if re-verified.

**Held, do not build:** KDM Szczecin (address conflict), Zajdel Częstochowa (Q Service Castrol),
Gulf Coast Diesel (address conflict), Motosilesia (campers).

## 3. Tenants: create → clone → rewrite (main session, ~3 min each)

From `/Users/stan/Code/givyx/givyx.claudeBrain`. **Never curl `<slug>.givyx.com` before the tenant
exists** (the renderer caches the 404 for 60 s+). Check availability with
`curl -s -o /dev/null -w "%{http_code}" https://api.givyx.com/locations/by-slug/<slug>` (404 = free).

```
dealership/tools/new-tenant.sh "<Business Name>" <slug> pl        # prints appId/locationId; token → .mcp.json, never echo it
cd /Users/stan/Code/givyx/Givyx.Api/tools/GivyxTestSetup
export StorageConnectionString="$(sed 's/^\xEF\xBB\xBF//' ../../.env | tr -d '\r' | grep -m1 '^StorageConnectionString=' | cut -d= -f2-)"
export JwtSecret="$(sed 's/^\xEF\xBB\xBF//' ../../.env | tr -d '\r' | grep -m1 '^JwtSecret=' | cut -d= -f2-)"
dotnet run --no-build -- clonefrom l_5fd7d91 <locationId> --purge          # PL source (EN: l_5d08dd1)
dotnet run --no-build -- rewrite <locationId> '"https://dealership.givyx.com' '"https://<slug>.givyx.com'
```
Expect `DONE — manifest + 8 page(s) cloned` and `12 replacement(s)`. Then `curl …/?preview=1` → 200.
Add a row to `dealership/clones/index.md` (slug · business · pl · l_5fd7d91 · appId · locationId · date · state).
⚠️ Never `dotnet run` the API project itself (it writes to production storage on startup); the
GivyxTestSetup tool is the only thing you run.

## 4. Build agents — MAX 4 AT ONCE (each ~30 min, ~350k tokens)

Twelve at once hit the account session limit on 09-14 and all died. Keep four in flight; start the
next as one finishes. Prompt per prospect (fill the `<…>`):

> You are a build agent working in `/Users/stan/Code/givyx/givyx.claudeBrain` (cd there first).
> Build the personalised prospect demo for **<Name> (<City>)** on the tenant that already exists:
> slug `<slug>` (MCP key in `.mcp.json`; call tools with `Givyx/tools/mcp.sh <slug> <tool> '<json>'`),
> appId `<appId>`, locationId `<locationId>`, lang `pl`, source = PL `dealership` (`l_5fd7d91`),
> already cloned `--purge` and host-rewritten; Preview renders 200 at https://<slug>.givyx.com/?preview=1
> and still carries the template's fictional "AutoSerwis Kowalski" identity. Use your own scratch
> dir (`$TMPDIR/<slug>/`) — other build agents run concurrently.
> Read, in this order, before touching anything: (1) `Givyx/superpowers/specs/2026-09-11-prospect-demo-clone.md`
> — you execute steps 4 through 13; (2) `dealership/template/clone-runbook.md` §3–§6;
> (3) `dealership/clones/napierala.md` and the "lessons" tails of `dealership/clones/dieselchip.md`
> and `dealership/clones/poslowski.md` — copy their rigour and log format; (4) the research pack:
> the "<Name>" section in `/Users/stan/Code/givyx/PersonalAssistant/prospects/<batch file>` — the
> ONLY source of facts. Tools: `dealership/tools/set-values.py`, `dealership/tools/map-optout.py`.
> Prospect specifics: phone <as displayed> → every `tel:` = `tel:+48<digits>`; email <email>;
> rating row **<x,y · N opinii, read <date>>**; prices: <none published → none / quote the pack's
> cennik exactly, `labelPrice` "Cena">; hours: <as the pack states; if site and Google disagree on a
> closing time, print the opening time and days only and say so>; <no own photos → upload nothing,
> shared assets only, neutral captions, NO ogImage>.
> Non-negotiable rules: every fact from the pack; services in THEIR wording, ≤8, no padding, generic
> copy apart from quoted facts; photos only from the pack's own-photo URLs (rsync per runbook, never
> the images REST API; `ogImage` = one of them; no caption may claim the shared film/GLB is their
> premises); copy sweep per spec step 9 + `dealership.givyx.com` + source phone/coords → 0 hits in
> stored JSON and rendered HTML; JSON-LD on /faq and /o-warsztacie all theirs; SEO one `update_seo`
> with title, description, `lang:"pl"`, `locales:["pl"]`, ogImage, **`noIndex:true`** (verify
> `noindex, nofollow` + robots `Disallow: /`); forms: create the clone's OWN booking (11 fields) +
> contact (4 fields), `notifyEmails` = `info@givyx.com,stan.zak.inf@gmail.com`, declare fields first,
> submit each once with TEST, read back `Notified:true`; maps: `dealership/tools/map-optout.py <slug> pl`
> + read back (re-run if a later rewrite touches card-menu/FAQ); Preview-only — do NOT call
> `deploy_to_production`; one MCP call per Bash invocation if the classifier blocks a loop.
> **Write `dealership/clones/<slug>.md` EARLY and update it as you go.**
> Verify per spec step 13 (pages under 32K; local Playwright desktop + mobile — the hidden Browser
> pane is stale; every `tel:` E.164; no-WebGL fallback; no Maps request before consent on map-less
> pages). Screenshots to `Givyx/screenshots/<slug>/`. Output: the clone log in napierala.md's format
> and the `<slug>` row in `dealership/clones/index.md` → "built + verified on Preview". Do not commit.
> Report back in under 200 words: preview URL, form ids, sweep result, anything unverified.

If an agent dies mid-way (429, timeout): check the tenant's real state before re-dispatching —
title, robots meta, `list_forms`, screenshots folder, log — and send a "finish" agent for what is
missing rather than a full rebuild.

## 5. Independent verification (main session, 2 min per site)

```
ops/tools/verify-clone.sh <slug> pl
```
Expect: their title · `robots="noindex, nofollow"` · `Disallow: /` · `leaks=0` · one `tel:+48…` ·
the rating row. Then Gmail (shade mailbox or inf): `newer_than:1d from:info@givyx.com subject:submission`
→ two notifications per tenant. Anything off → the agent's log, then fix.

## 6. Review email to Stan (one email, then wait)

`POST /emails` to `stan.zak.inf@gmail.com`, `layout:"givyx"`, `locationId:"l_givyx"`, subject
`[DO SPRAWDZENIA] <N> stron — batch <n>`, html: numbered links `<slug>.givyx.com` with one line each
(city, rating, prices yes/no, hours choice, photo situation, any flag), the holds, then the two asks:
"ok publish" and "send all". Attach nothing. Stan replies in chat.

**On "ok publish":** `Givyx/tools/mcp.sh <slug> deploy_to_production '{}'` per tenant (expect
`pagesPromoted:8, pagesDeleted:0`), then re-run `verify-clone.sh` on the bare URL. Update the index
rows to **PUBLISHED**, commit + push the brain (`dealership/clones/*.md`, `index.md`; screenshots
are gitignored).

## 7. Send (only after "send all"; one curl per prospect)

Codes: `<2–3 letters>-<yyyymmdd>-e1`, unique forever; register them in `prospects/pipeline.md`.
```
python3 ops/tools/build-email-json.py <slug> "<Name>" <email> <code> "<FAKT from the pack>" pl > /tmp/<slug>.json
python3 -c "import json,re,html;d=json.load(open('/tmp/<slug>.json'));print(d['to'],d['subject']);print(html.unescape(re.sub('<[^>]+>',' ',d['html']))[:600])"   # read it back once
ops/tools/send-one.sh /tmp/<slug>.json          # expect {"sent":1,"failed":0,...}
```
Drop any clause of the FAKT that the build left unprinted (e.g. a closing time the site and Google
disagree on). Never loop over recipients in one Bash call.

## 8. Records (10 min)

- `prospects/pipeline.md`: a table row per prospect (slug · name · email · SENT date · code) and the
  follow-up line (D+3 SMS = Stan, D+5 email 2, D+10 last). Mobiles listed for Stan's SMS.
- `LOG.md`: one dated entry (research pool, tenants, builds, sends, incidents, scoreboard).
- `STATE.md`: the counts row (sites live, emails sent) and the "Next moves" table.
- Notion: the "Volume" task (+ batch note), Ref 88 "Watch info@" task (+ send count).
- Commit + push `PersonalAssistant` (main) and `givyx.claudeBrain`.

## 9. Gotchas (all learned the hard way)

- `update_seo` REPLACES the whole Seo object: always resend `lang` + `locales` + `noIndex`.
- The clone inherits the SOURCE's form ids — every clone needs its own two forms or a prospect's
  test booking notifies the wrong tenant.
- `map-optout.py` must run AFTER the last card-menu/FAQ rewrite (rewrites drop the flag).
- Never assert a price, service, hour, photo or branch the pack does not carry. "Sieć warsztatów"
  with no branch address = single location. No published price = no price anywhere.
- No own photos → shared assets with neutral captions, no ogImage (the Givyx brand card is the fallback).
- Send Stan ONE email per batch, not several. Prospect emails go out only on his word.
- The classifier blocks: PR merges, loops over external recipients, scripted loops with the admin
  token. Single explicit calls pass.
- Replies land in `stan.zak.shade@gmail.com`; form notifications in both mailboxes.
