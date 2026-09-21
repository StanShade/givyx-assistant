"""Shared pieces of every Givyx offer e-mail (2026-09-21, Stan's OK on the v4.1 look):
pill CTA, signature by language, text/plain part, and the request envelope for POST /emails.
Both builders (build-email-v2.py personalised, build-email-v4.py generic) import from here so a
change to the signature or the button lands everywhere at once.

Look: "Oferta"/"Offer" is the header pill next to the logo (badge, not eyebrow); the shell's own
contact block is off (showContact:false, API PR #89) because the signature carries the contacts;
every mail goes out multipart/alternative — never HTML-only (Gmail Promotions/spam signal).
"""
import html as H, re

ACCENT, MUTED, RULE = "#0f7a5a", "#6b7a74", "#e3ebe7"
ICONS = "https://images.givyx.com/brand/givyx/ic-%s.png"
LOGO = "https://images.givyx.com/brand/givyx/sig-mark-128.png"   # rounded tile cut from givyx_logo_asset/cut/icon
PHONE, PHONE_TEL, EMAIL, SITE = "571 088 012", "+48571088012", "info@givyx.com", "https://givyx.com"
MAPS = "https://www.google.com/maps/search/?api=1&query=Karola+Bunscha+15A%2C+30-392+Krak%C3%B3w"
INSTAGRAM, LINKEDIN = "https://www.instagram.com/givyx.ai", "https://www.linkedin.com/company/givyx/"
ADDRESS = "Karola Bunscha 15A, 30-392 Kraków"

# Signature by language: name form, title and tagline all follow it. Never mix languages in one block.
SIG = {
    "pl": {"name": "Stanisław Zakharevich", "title": "Dyrektor, Givyx", "tagline": "Strony internetowe i aplikacje mobilne",
           "phone": "Telefon", "phone_show": PHONE, "map": ADDRESS, "badge": "Oferta"},
    "en": {"name": "Stan Zakharevich", "title": "Director, Givyx", "tagline": "Websites & mobile apps",
           "phone": "Phone", "phone_show": "+48 " + PHONE, "map": ADDRESS + ", Poland", "badge": "Offer"},
    "ru": {"name": "Слава Захаревич", "title": "Директор, Givyx", "tagline": "Сайты и мобильные приложения",
           "phone": "Телефон", "phone_show": "+48 " + PHONE, "map": ADDRESS, "badge": "Предложение"},
}

def tagged(url, medium, campaign):
    """UTM for our analytics. It stores utm_source/medium/campaign only (utm_content is dropped), so the
    prospect code goes in utm_campaign — that is the only way a click stays attributable to one mail."""
    return f"{url}{'&' if '?' in url else '?'}utm_source=email&utm_medium={medium}&utm_campaign={campaign}"

def p(t): return f"<p>{t}</p>"
def ul(items): return '<ul style="margin:6px 0 14px;padding-left:20px">' + "".join(f"<li style='margin:3px 0'>{i}</li>" for i in items) + "</ul>"

def cta(url, label, hint):
    """Pill button: solid green for Outlook, a soft gradient where the client allows background-image."""
    return ('<!--cta-->'
            '<table role="presentation" width="100%" cellspacing="0" cellpadding="0"><tr>'
            '<td align="center" style="padding:22px 0 6px">'
            '<table role="presentation" cellspacing="0" cellpadding="0" style="width:auto;margin:0 auto"><tr>'
            # class="btn": the shell's dark-mode rule for `.btn a` keeps the label readable on the green
            f'<td class="btn" style="background:{ACCENT};background-image:linear-gradient(180deg,#149470 0%,{ACCENT} 100%);'
            'border-radius:999px;box-shadow:0 8px 20px rgba(15,122,90,0.30)">'
            f'<a href="{H.escape(url)}" style="display:inline-block;box-sizing:border-box;text-align:center;padding:17px 32px;color:#ffffff;'
            f'font-weight:700;text-decoration:none;font-size:16px;line-height:1.3;letter-spacing:0.01em;border-radius:999px">{label}</a>'
            '</td></tr></table>'
            f'<div style="font-size:13px;color:{MUTED};margin-top:12px">{hint}</div>'
            '</td></tr></table>'
            f'<!--/cta {H.escape(url)}-->')

def icon(name, href, title):
    return (f'<td style="padding-right:8px"><a href="{H.escape(href)}" title="{title}" style="text-decoration:none">'
            f'<img src="{ICONS % name}" width="34" height="34" alt="{title}" style="display:block;border:0;width:34px;height:34px"></a></td>')

def signature(lang, code):
    """`code` = the prospect's e-mail code: the givyx.com links (logo + globe) are tagged with it, so a
    click from the signature shows up on tenant l_givyx as campaign <code>, medium "signature".
    Phone/WhatsApp/mail/Instagram/LinkedIn/Maps leave our domain and cannot be tracked."""
    t = SIG[lang]
    site = tagged(SITE + "/", "signature", code)
    links = (icon("phone", f"tel:{PHONE_TEL}", f"{t['phone']}: {t['phone_show']}")
             + icon("whatsapp", f"https://wa.me/{PHONE_TEL.lstrip('+')}", "WhatsApp")
             + icon("mail", f"mailto:{EMAIL}", EMAIL)
             + icon("globe", site, "givyx.com")
             + icon("instagram", INSTAGRAM, "Instagram")
             + icon("linkedin", LINKEDIN, "LinkedIn")
             + icon("pin", MAPS, t["map"]))
    # Icons go under the logo/name row, not beside it: seven tiles plus the logo do not fit a phone.
    return ('<!--sig-->'
            f'<hr style="border:0;border-top:1px solid {RULE};margin:26px 0 18px">'
            '<table role="presentation" cellspacing="0" cellpadding="0" style="width:auto"><tr>'
            f'<td style="vertical-align:top;padding-right:14px;width:64px"><a href="{H.escape(site)}"><img src="{LOGO}" width="64" height="64" alt="Givyx" '
            'style="display:block;border:0;width:64px;height:64px"></a></td>'
            '<td style="vertical-align:middle">'
            f'<p style="margin:0 0 2px;line-height:1.35"><strong style="font-size:16px">{t["name"]}</strong><br>'
            f'<span style="font-size:14px;color:{MUTED}">{t["title"]}</span></p>'
            f'<p style="margin:0;font-size:13px;line-height:1.5;color:{MUTED}">{t["tagline"]}</p>'
            '</td></tr></table>'
            f'<table role="presentation" cellspacing="0" cellpadding="0" style="width:auto;margin-top:14px"><tr>{links}</tr></table>'
            '<!--/sig-->')

def signature_text(lang):
    t = SIG[lang]
    return (f"--\n{t['name']}\n{t['title']}\n{t['tagline']}\n"
            f"{t['phone_show']} ({t['phone']}/WhatsApp) · {EMAIL} · givyx.com\n{INSTAGRAM} · {LINKEDIN}\n{t['map']}\n")

def to_text(body, lang, title=None):
    """text/plain twin of a body built from p/ul/cta/signature: the CTA becomes its bare URL, the
    signature its text form, everything else loses its tags."""
    t = re.sub(r"<!--cta-->.*?<!--/cta (.*?)-->", lambda m: f"\n{H.unescape(m.group(1))}\n", body, flags=re.S)
    t = re.sub(r"<!--sig-->.*?<!--/sig-->", "\n" + signature_text(lang), t, flags=re.S)
    t = re.sub(r"<li[^>]*>", "- ", t)
    t = re.sub(r"</li>", "\n", t)
    t = re.sub(r"</(p|ul|div)>", "\n\n", t)
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = H.unescape(t)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"
    return (f"{title}\n\n{t}" if title else t)

def request(to, subject, title, body, lang):
    return {"to": [to], "subject": subject, "layout": "givyx", "locationId": "l_givyx",
            "eyebrow": "", "title": title, "badge": SIG[lang]["badge"], "showContact": False,
            "replyTo": EMAIL, "html": body, "text": to_text(body, lang, title)}
