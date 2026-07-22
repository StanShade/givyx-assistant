# Shared tail appended to every prospect config (photos + theme + callback form defaults).
# The build reads config.py as a standalone module, so each prospect config is made
# self-contained by concatenating this block. Values identical to the AutoSerwis base.
#
# EVERYTHING here is a DEFAULT. The head is concatenated BEFORE this block, so every
# assignment below is guarded with `if "X" not in globals():` — a head that defines its
# own value wins, and heads that define none resolve exactly as they did before.

# ---- callback form ----
if "FORM_SLUG" not in globals():
    FORM_SLUG = "oddzwonimy"
if "FORM_NAME" not in globals():
    FORM_NAME = "Oddzwonimy — callback"
if "FORM_HEADLINE" not in globals():
    FORM_HEADLINE = "Zostaw numer — oddzwonimy do 15 min"
if "FORM_SUB" not in globals():
    FORM_SUB = "w godzinach pracy"
if "FORM_SUCCESS" not in globals():
    FORM_SUCCESS = "Dziękujemy! Oddzwonimy do 15 minut w godzinach pracy."
if "FORM_SUBMIT" not in globals():
    FORM_SUBMIT = "Zamów rozmowę"
if "FORM_FOOTER" not in globals():
    FORM_FOOTER = "Wysyłając numer zgadzasz się na kontakt telefoniczny w sprawie Twojego zapytania."
# Owner-notification recipients (comma separated). Empty means a real lead is stored
# with NOBODY notified — on 2026-07-21 all three previews shipped that way. During the
# preview phase this must be OUR address, not the prospect's: he has not signed yet.
if "FORM_NOTIFY_EMAILS" not in globals():
    FORM_NOTIFY_EMAILS = "stan.zak.inf@gmail.com"
if "SERVICES_NOTE" not in globals():
    SERVICES_NOTE = "Nie widzisz swojej usterki? Zadzwoń — powiemy od razu, czy pomożemy i ile to kosztuje."
if "REVIEWS_BADGE" not in globals():
    REVIEWS_BADGE = "Opinie z Google"

# ---- photos (Unsplash, host allowlisted in givyx.websites) ----
# A head that serves a shop with a different trade (e.g. a tyre-only shop) must
# override these — captioning a service the shop does not offer is exactly as
# dishonest as writing it in the copy.
#
# Head overrides (all optional):
#   HERO_BG_ID   = "photo-..."             # unsplash id, rendered at 1800w
#   HERO_BG      = "https://..."           # or the full URL, if you need custom params
#   VISIT_PHOTO  = ("photo-...", w, h)     # or a full https:// URL in place of the id
#   VISIT_ALT    = "..."                   # alt text for the home "visit" photo
#   GALLERY      = [("photo-...", "Caption"), ...]   # captions must match real services
#   GALLERY_W, GALLERY_H = 800, 600
# Allowlisted hosts: images.unsplash.com, images.givyx.com, givyx.blob, shade.blob.
# plus.unsplash.com premium photos are NOT allowlisted — they will not load.
def u(pid, w, h=None):
    """Unsplash CDN URL — or the value itself when a head passes a full URL
    (real photos uploaded to images.givyx.com need no resize params)."""
    if str(pid).startswith("http"):
        return pid
    hp = f"&h={h}" if h else ""
    return f"https://images.unsplash.com/{pid}?q=75&w={w}{hp}&auto=format&fit=crop"

if "HERO_BG" not in globals():
    if "HERO_BG_ID" not in globals():
        HERO_BG_ID = "photo-1625047509168-a7026f36de04"   # dark workshop bay
    HERO_BG = u(HERO_BG_ID, 1800)

if "VISIT_PHOTO" not in globals():
    VISIT_PHOTO = ("photo-1615906655593-ad0386982a0f", 900, 700)
if "VISIT_ALT" not in globals():
    VISIT_ALT = "Mechanik przy silniku w hali serwisowej"

if "GALLERY" not in globals():
    GALLERY = [
        ("photo-1615906655593-ad0386982a0f", "Diagnostyka pod maską"),
        ("photo-1625047509168-a7026f36de04", "Hala serwisowa"),
        ("photo-1530046339160-ce3e530c7d2f", "Narzędziownia"),
        ("photo-1487754180451-c456f719a1fc", "Wymiana oleju"),
        ("photo-1486262715619-67b85e0b08d3", "Serwis osprzętu silnika"),
        ("photo-1632823469850-2f77dd9c7f93", "Dbałość o detale"),
    ]
if "GALLERY_W" not in globals():
    GALLERY_W = 800
if "GALLERY_H" not in globals():
    GALLERY_H = 600

# ---- theme / palette ----
if "BG0" not in globals():
    BG0 = "#0B0E11"
if "BG1" not in globals():
    BG1 = "#10141A"
if "CARD" not in globals():
    CARD = "#151B22"
if "BORDER" not in globals():
    BORDER = "#242C36"
if "FG" not in globals():
    FG = "#F2F4F6"
if "MUTED" not in globals():
    MUTED = "#9AA6B2"
if "ACCENT" not in globals():
    ACCENT = "#F5A524"
if "ACCENT_INK" not in globals():
    ACCENT_INK = "#14181D"
if "BTN_FORM" not in globals():
    BTN_FORM = "#E8590C"
if "OK_GREEN" not in globals():
    OK_GREEN = "#4ADE80"

# ---- reviews: HONEST DEFAULT — no fabricated testimonials ----
# We do NOT invent named reviews. When REVIEWS is empty, the template renders the real
# Google rating (REVIEWS_SUBHEAD) + a "Zobacz opinie w Google" button linking to MAPS_URL.
# Real quotes get added after the owner signs (part of the maintenance service).
# A shop with no refreshed rating sets SHOW_REVIEWS = False and the section is dropped —
# better an absent section than a number we cannot stand behind.
if "REVIEWS" not in globals():
    REVIEWS = []
if "GOOGLE_REVIEWS_URL" not in globals():
    GOOGLE_REVIEWS_URL = MAPS_URL       # opens the shop's real Google listing/reviews
if "GOOGLE_REVIEWS_CTA" not in globals():
    GOOGLE_REVIEWS_CTA = "Zobacz opinie w Google"
