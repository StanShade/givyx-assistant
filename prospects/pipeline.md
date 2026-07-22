# Sales Pipeline — Wave 1 (Kraków car services)

Stages: listed → preview built → contacted → replied → call/meeting → CLIENT (or dead + reason).
Update after every touch. Weekly totals go to LOG.md.

## Demo master (clone source for all previews)
- AutoSerwis Kowalski built on sandbox l_96b5185 (slug `shade`) — preview:
  https://shade.givyx.com/?preview=1 (bare URL still serves old demo until Stan publishes).
- Clone playbook: edit `givyx.claudeBrain/Givyx/demos/autoserwis/config.py`, point GIVYX_TOKEN at
  target location, `./run.sh` (~5 min, tenant-agnostic). Finding: Givyx/findings/2026-07-17-autoserwis-demo-build.md.
- Stan actions: (1) `deploy_to_production` for l_96b5185 to serve publicly (agents blocked from it);
  (2) optional `moto.givyx.com` — create location slug `moto` in Portal, mint token.

## ⚠️ VERIFIED RE-RANK 2026-07-20 — build previews for THESE first
| Rank | Prospect | Phone | Verified problem (provable) |
|---|---|---|---|
| 1 | **Tłumiki Bielarz** | 601 489 603 | 4,8★/308 reviews BUT cert expired May-2024 & belongs to andrzejkrupinski.net; no mobile viewport — ✅ PREVIEW LIVE https://tlumiki.givyx.com (loc l_fe8c1fc) — **📤 SMS SENT 2026-07-20 (first ever outreach)** → awaiting reply |
| 2 | **D.W. Serwis** ⭐ NOW #1 TARGET | 502 402 802 | 4,8★/282 opinii AND their Google listing still says "dodaj stronę" (site not attached) + $680/mo gym plans on the homepage. Every clause owner-verifiable in 10s. Preview: dwserwis.givyx.com (l_0a88148) — ⚠️ imagery fix in progress before send |
| 3 | **ZUW Opony i Felgi** | 12 658 74 27 | Since 1980, 16 tyre brands, Goodyear+Dębica dealer, 4,3★/117 — site is a MS Publisher 2003 export, no mobile, HTTPS blocked. Preview: oponyifelgi.givyx.com (l_ba863f2) — ⚠️ HOURS UNCONFIRMED + imagery fix before send |
| — | ~~All Cars Service~~ | — | ❌ REMOVED — owns a modern site WITH booking. Do not contact. |
| — | Intra Cars | 12 311 02 01 | Downgraded: has 2 working microsites, one WITH booking. Pitch = ownership only. |

Configs ready: previews/heads/tlumiki.py, oponyifelgi.py, dwserwis.py (all corrected with verified data).

## Wave 1 targets (ORIGINAL top 10 — superseded by the re-rank above)

| # | Prospect | Stage | Preview URL | Last touch | Next action | Notes |
|---|----------|-------|-------------|-----------|-------------|-------|
| 1 | Intra Cars (424 reviews!) | PREVIEW BUILT ✅ | intracars.givyx.com/?preview=1 (l_2de5017) | 2026-07-18 | Stan: confirm ⚠️ items, flip noindex, deploy_to_production | verified render + form (resp_0a970291) |
| 2 | All Cars Service | listed | — | — | build preview | 12 yrs, 5.5★, has email |
| 3 | M-TRAK | listed | — | — | build preview | niche: podwozia |
| 4 | Serwis Aut Francuskich Piekara | listed | — | — | build preview | 25 yrs French cars, has email |
| 5 | Speed-Gum | listed | — | — | build preview | 5.0★, has email |
| 6 | D.W. Serwis | listed | — | — | build preview | site shows GYM pricing — killer opener |
| 7 | Tłumiki Bielarz | listed | — | — | build preview | SSL-dead domain opener |
| 8 | Opony i Felgi ZUW | listed | — | — | build preview | SSL-dead domain opener |
| 9 | Auto-Service Fijałków | listed | — | — | build preview | SSL-dead; Nowa Huta anchor |
| 10 | Auto-Moto-Max (2 locations) | listed | — | — | build preview | 1 site serves 2 shops |

## Bench (contact without preview, SMS 1b)
11 Binkuś (klima) · 12 Cool-Car · 13 Auto Styl (oklejanie) · 14 De Vito · 15+ rest of Tier 2
(verify each on Google Maps 30s before texting).

## Wave 1 funnel
| Metric | Target | Actual |
|--------|--------|--------|
| Demo master built | 1 | 1 ✅ |
| Previews built | 10 | 2 (Intra Cars, Tłumiki Bielarz) |
| **SMS SENT** | 1 | **2** ✅ Bielarz 2026-07-20 · D.W. Serwis 2026-07-21 |
| **CALLS made** | — | **1** — ZUW 2026-07-22, reached, declined |
| **Live conversations** | ≥1 | **2 ✅** — ZUW (declined) · Speed-Gum (asked for the offer) |
| **Offers sent** | — | **1** — Speed-Gum 2026-07-22, personalised site + 3 tiers |
| Replies | ≥1 | 0 (waiting) |
| Calls/meetings | ≥1 | 0 |
| Clients | 1 | 0 |

## 📤 Wave 1 — send log
| Date | Prospect | Channel | Message | Outcome |
|---|---|---|---|---|
| 2026-07-20 | Tłumiki Bielarz (601 489 603) | SMS from Stan's phone | "4,8★/308 opinii… certyfikat wygasł w 2024… podgląd: tlumiki.givyx.com" | ❌ no reply (Stan: moving on 2026-07-21; may phone them himself). Preview since rebuilt — the 4 invented facts he was originally sent are gone. |
| **2026-07-22** | **Speed-Gum Serwis Opon (Tomasz Gil, 537 326 327)** | ☎️ CALL → 📧 EMAIL | Call: first „nie", turned into **„proszę wysłać ofertę z przykładem"**. Then a personalised site built + emailed to speed-gum@op.pl with 149/249/750 | ⏳ **awaiting reply** — warmest contact we have. He ASKED for this, so it is a kept promise, not cold outreach |
| **2026-07-22** | **ZUW Opony i Felgi (504 121 596)** | ☎️ **CALL — first live conversation ever** | Direct opener: „czy chcieliby Państwo mieć własną profesjonalną stronę?" | ❌ **„Nie dziękuję, nie jestem zainteresowany."** Landline 12 658 74 27 dead; reached them on the directory mobile. **CLOSED — do not call again, do not send the preview.** |
| **2026-07-21** | **D.W. Serwis (502 402 802)** | SMS from Stan's phone | "4,8★/282 opinie… pod „Najpopularniejsze usługi" karnety na siłownię $680 per month… podgląd: dwserwis.givyx.com" | ⏳ **awaiting reply** — hook re-verified same day, preview rebuilt + all 4 pages verified |
| Contacted (SMS/email) | 20 | 0 |
| Replies | ≥5 | 0 |
| Calls/meetings | ≥2 | 0 |
| Clients | 1 | 0 |

## Rules
- Max 10–20 first-touches/day, always personalized (hooks in krakow-car-services.md).
- SMS from Stan's real number; STOP opt-out honored immediately (note in table).
- Every reply gets an answer same day.
