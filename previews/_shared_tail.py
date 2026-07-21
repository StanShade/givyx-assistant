# Shared tail appended to every prospect config (photos + theme + callback form defaults).
# The build reads config.py as a standalone module, so each prospect config is made
# self-contained by concatenating this block. Values identical to the AutoSerwis base.

# ---- callback form ----
FORM_SLUG = "oddzwonimy"
FORM_NAME = "Oddzwonimy — callback"
FORM_HEADLINE = "Zostaw numer — oddzwonimy do 15 min"
FORM_SUB = "w godzinach pracy"
FORM_SUCCESS = "Dziękujemy! Oddzwonimy do 15 minut w godzinach pracy."
FORM_SUBMIT = "Zamów rozmowę"
FORM_FOOTER = "Wysyłając numer zgadzasz się na kontakt telefoniczny w sprawie Twojego zapytania."
SERVICES_NOTE = "Nie widzisz swojej usterki? Zadzwoń — powiemy od razu, czy pomożemy i ile to kosztuje."
REVIEWS_BADGE = "Opinie z Google"

# ---- photos (Unsplash, host allowlisted in givyx.websites) ----
# The head is concatenated BEFORE this block, so every photo value below is a DEFAULT:
# it is only assigned when the head did not already define it. A head that serves a shop
# with a different trade (e.g. a tyre-only shop) must override these — captioning a
# service the shop does not offer is exactly as dishonest as writing it in the copy.
#
# Head overrides (all optional):
#   HERO_BG_ID   = "photo-..."             # unsplash id, rendered at 1800w
#   HERO_BG      = "https://..."           # or the full URL, if you need custom params
#   VISIT_PHOTO  = ("photo-...", w, h)
#   VISIT_ALT    = "..."                   # alt text for the home "visit" photo
#   GALLERY      = [("photo-...", "Caption"), ...]   # captions must match real services
#   GALLERY_W, GALLERY_H = 800, 600
# Only images.unsplash.com is allowlisted by the renderer (plus givyx.blob,
# shade.blob, images.givyx.com) — plus.unsplash.com premium photos will NOT load.
def u(pid, w, h=None):
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
BG0 = "#0B0E11"; BG1 = "#10141A"; CARD = "#151B22"; BORDER = "#242C36"
FG = "#F2F4F6"; MUTED = "#9AA6B2"; ACCENT = "#F5A524"; ACCENT_INK = "#14181D"
BTN_FORM = "#E8590C"; OK_GREEN = "#4ADE80"

# ---- reviews: HONEST DEFAULT — no fabricated testimonials ----
# We do NOT invent named reviews. When REVIEWS is empty, the template renders the real
# Google rating (REVIEWS_SUBHEAD) + a "Zobacz opinie w Google" button linking to MAPS_URL.
# Real quotes get added after the owner signs (part of the maintenance service).
REVIEWS = []
GOOGLE_REVIEWS_URL = MAPS_URL           # opens the shop's real Google listing/reviews
GOOGLE_REVIEWS_CTA = "Zobacz opinie w Google"
