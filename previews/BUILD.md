# Preview build guide (C4) — batch of 10 Kraków car-service previews

Each preview = the AutoSerwis Kowalski demo cloned with a prospect config.

## Config files
- **Intra Cars**: `previews/intracars-config.py` — complete BUT relies on base for photos/theme
  (the intracars build agent appended those). For the other 9, use the head+tail split below.
- **Other 9**: `previews/heads/<slug>.py` (identity + services + SEO) — must be concatenated with
  `previews/_shared_tail.py` (photos + theme + form + reviews + u() helper) to form a complete config.py.

Slugs: allcars, mtrak, piekara, speedgum, dwserwis, tlumiki, oponyifelgi, fijalkow, automotomax.

## ⛔ The clone is BUILD OUTPUT — never hand-edit it

A clone (`autoserwis-<slug>/`) must be reproducible from `autoserwis/` + head + tail, and nothing
else. **All per-shop copy belongs in the head file.** On 2026-07-21 the dwserwis and oponyifelgi
clones had their H1, hero eyebrow/sub, section headings, footer lines and a whole info strip
hand-edited into `build_pages.py`/`build_chrome.py` — text that existed nowhere else. A fresh
`cp -r` (which BUILD.md itself mandates) would have silently reverted both previews to generic
template copy. Those values now live in the heads, and the base builders read them via
`lib.copy(KEY, default)`.

If the template can't express something, **add a config key to the base builder** — do not edit
the clone. Before any rebuild, diff the clone against the base and check nothing is clone-only:
```
diff -r givyx.claudeBrain/Givyx/demos/autoserwis-<slug> givyx.claudeBrain/Givyx/demos/autoserwis \
  --exclude=config.py --exclude=__pycache__ --exclude=_form_id.txt
```

### Copy keys a head may set (all optional; every default is true-by-construction)
| key | default |
|---|---|
| `HERO_EYEBROW` | `Warsztat samochodowy · {DISTRICT}` |
| `HERO_H1` | `Naprawimy Twoje auto. Szybko i uczciwie.` |
| `HERO_SUB` | first 4 `SERVICES` names + "— w jednym miejscu…" |
| `HOME_SERVICES_EYEBROW` / `_TITLE` / `_LEAD` | price-aware: drops all price wording when no service publishes one |
| `USLUGI_LABEL` | `Usługi i cennik` **only if** a service carries a digit, else `Usługi` |
| `USLUGI_SUBHEAD` / `USLUGI_LEAD` | `Zakres naszych usług` / price-aware lead |
| `GALERIA_TITLE` / `GALERIA_LEAD` | `Tak wygląda nasza robota` / `Zdjęcia poglądowe usług…` |
| `FOOTER_TAG` / `FOOTER_DESC` | district line / first 3 `SERVICES` names |
| `INFO_STRIP` | none (section omitted) |

`lib.has_prices()` is the single source of truth for "does this shop publish prices" — it looks for
a digit in the price column of `SERVICES`. Nothing may say *cennik* or *ceny „od”* when it is False.

## Per-prospect build (run by an executor agent in givyx.claudeBrain)
For each slug S with its location-scoped MCP token T (Stan mints one per slug in Portal):
```
cp -r givyx.claudeBrain/Givyx/demos/autoserwis givyx.claudeBrain/Givyx/demos/autoserwis-S
cat PersonalAssistant/previews/heads/S.py PersonalAssistant/previews/_shared_tail.py \
    > givyx.claudeBrain/Givyx/demos/autoserwis-S/config.py
cd givyx.claudeBrain/Givyx/demos/autoserwis-S
python3 -c "import config"                 # must succeed — no NameError
export GIVYX_TOKEN='T' && ./run.sh
```
Then verify https://S.givyx.com/?preview=1 (mobile+desktop screenshot, submit callback form once),
save shots under givyx.claudeBrain/Givyx/screenshots/S/. Do NOT deploy_to_production (Stan does that).

**Verify every page, not just the home page.** On 2026-07-21 both tyre-shop previews had a correct
home page and a `/galeria` still reading *"Zajrzyj do naszej hali"* with captions *Wymiana oleju*,
*Diagnostyka pod maską* and *Serwis osprzętu silnika* — on shops that only touch tyres. The home
page had been rebuilt; the rest of the site had not. Fetch `/`, `/uslugi`, `/galeria` and `/kontakt`.

A token-free pre-flight that renders every page tree offline and fails on any service the config
never claimed, any invented `zł`, and any *cennik* without prices:
`previews/tools/verify_copy.py <slug>` — run it before spending a token on a push.
`previews/tools/compare_live.py <slug>` diffs the offline render against the live site, so you can
see exactly what a rebuild would add or lose before pushing.

## What Stan provides
- One location per slug (Portal → create location with that slug) + one MCP token per location.
- After each preview verifies, Stan runs deploy_to_production for that location to serve it publicly.

## ⛔ Imagery must be the shop's OWN — stock is no longer a default (2026-09-10)

`_shared_tail.py` used to ship a **generic mechanic** photo set as the `GALLERY` default, which the
gallery page then headed *"Tak wygląda nasza robota"* — stock photos captioned as the shop's own
work, on four live previews. `build_pages.py:457` already carried a comment forbidding exactly that
while the default underneath it did it anyway.

**Two guards now enforce it:**
1. `GALLERY` has **no default**. A head must set either real photos or an explicit `GALLERY = []`.
2. `tools/verify_copy.py` fails any render whose imagery is not on `images.givyx.com`, and fails
   harder when a first-person caption ("nasza robota") sits over foreign imagery.
3. `build_seo.py` refuses to publish a non-own image as `ogImage`/`LocalBusiness.image` — those are
   published **as the business** by Google and every social preview. Set `OG_IMAGE` in the head.

`GALERIA_TITLE`/`GALERIA_LEAD` now default to ownership-neutral copy. A head with verified photos
of its own may override with first-person wording (see `heads/speedgum.py`).

**Where photos come from:** the shop's own — sent by the owner, or their existing site/GBP shown
back to them in the pitch. Upload to `images.givyx.com`; only then may they carry a first-person
caption. `HERO_BG` and `VISIT_PHOTO` are still stock on most heads — `verify_copy.py` reports them.

### How the guards interact with the head/tail split

The tail is concatenated AFTER the head, so each value is guarded with `if "X" not in globals():` —
a head that defines its own imagery wins. That is why guard 1 alone is not enough: **`dwserwis`,
`tlumiki` and `oponyifelgi` each set their own Unsplash ids**, so they sail past a missing-default
check. Guard 2 (`verify_copy.py`) is what catches them.

Head-side overrides (all optional):

| key | shape | notes |
|---|---|---|
| `HERO_BG_ID` | `"photo-…"` | rendered at 1800w by the tail |
| `HERO_BG` | full URL | only if you need custom params; wins over `HERO_BG_ID` |
| `VISIT_PHOTO` | `("photo-…", w, h)` | home "Dojazd" photo |
| `VISIT_ALT` | `str` | alt text for that photo (build_pages reads it via `getattr`) |
| `GALLERY` | `[("photo-…", "Caption"), …]` | any length |
| `GALLERY_W`, `GALLERY_H` | ints | default 800×600 |

Rules:
- **Renderer allowlist:** `images.givyx.com`, givyx.blob, shade.blob, `images.unsplash.com`.
  `plus.unsplash.com/premium_photo-…` is NOT allowlisted — it will not load.
  **Allowlisted ≠ permitted:** unsplash still loads, but `verify_copy.py` now fails the build for it.
- **Never caption a service the shop doesn't offer.** Fetch and *look at* each photo before
  using it; Unsplash alt text is often wrong or the shot is a 3D render.
- Fewer correct photos beat more wrong ones. Dropping the Galeria page is acceptable.
- Overridden so far: `dwserwis`, `oponyifelgi` (both tyre-only shops).

## ⛔ Map coordinates are a fact like any other — geocode, never estimate

The `givyx-map` component (branch `feat/givyx-map`, not merged yet) takes `lat`/`lon`. **A coordinate
is exactly the kind of fact the never-invent rule covers, and it's the worst one to get wrong:** a pin
in the wrong place is visible in one glance, on the owner's own street, and it is the single most
checkable claim on the page. "About right for the district" is not good enough.

- Geocode the shop's **verified street address** and confirm the result — don't reuse a city-centre
  or district-centre coordinate. The `50.0651, 19.9553` in the component's docs is a **test fixture**
  for Kraków-Grzegórzki, not a real position for any prospect. Never ship it.
- If the address itself is still `⚠️CONFIRM`, do not add a map at all. `givyx-map` degrades on
  purpose: with no `lat`/`lon` it renders the address card and the directions link and **omits the
  map button entirely**, which is the correct output for an unverified location.
- Sanity-check every pin by opening it before the preview goes out, same as fetching and *looking at*
  each photo.

## Data quality
Every head file flags `# ⚠️CONFIRM` on postal codes, some emails, and hours (best-guess from public
listings). Prices/reviews are illustrative — the outreach SMS frames the preview as an adjustable
draft, and the owner confirms real details before go-live. Never present illustrative data as the
shop's real published numbers.
