#!/usr/bin/env python3
"""Build one POST /emails request for the GENERIC offer, v4 (2026-09-21, Stan's OK):
no per-prospect site, one demo link per niche, the personalised version is offered on reply.

v4.1 (21 Sep, Stan): "Oferta" as the header pill next to the logo (not an eyebrow), pill CTA,
signature under a rule (logo, "Stanisław Zakharevich / Director of Givyx", tagline, icon-only links:
phone, WhatsApp, mail, site, Instagram, LinkedIn, map) instead of the shell's contact block
(`showContact:false`, API PR #89), and a text/plain part so the mail goes out multipart/alternative.

usage: build-email-v4.py niche.json prospect.json > out.json
niche    = {"campaign","demo_url","subject","intro","link_hint","closing","title_prefix"}   (outreach/niches/<niche>.json)
prospect = {"name","to","code"}
"""
import html as H, json, re, sys

ACCENT, MUTED, RULE = "#0f7a5a", "#6b7a74", "#e3ebe7"
ICONS = "https://images.givyx.com/brand/givyx/ic-%s.png"
PHONE, PHONE_TEL, EMAIL, SITE = "571 088 012", "+48571088012", "info@givyx.com", "https://givyx.com"
MAPS = "https://www.google.com/maps/search/?api=1&query=Karola+Bunscha+15A%2C+30-392+Krak%C3%B3w"
INSTAGRAM, LINKEDIN = "https://www.instagram.com/givyx.ai", "https://www.linkedin.com/company/givyx/"
LOGO = "https://images.givyx.com/brand/givyx/sig-mark-128.png"   # rounded tile cut from givyx_logo_asset/cut/icon
TAGLINE = "Givyx — strony internetowe i rezerwacje online dla lokalnych firm · Kraków"

def cta(url, label, hint):
    # Pill button: solid green for Outlook, a soft gradient where the client allows background-image.
    return ('<table role="presentation" width="100%" cellspacing="0" cellpadding="0"><tr>'
            '<td align="center" style="padding:22px 0 6px">'
            '<table role="presentation" cellspacing="0" cellpadding="0" style="width:auto;margin:0 auto"><tr>'
            # class="btn": the shell's dark-mode rule for `.btn a` keeps the label readable on the green
            f'<td class="btn" style="background:{ACCENT};background-image:linear-gradient(180deg,#149470 0%,{ACCENT} 100%);'
            'border-radius:999px;box-shadow:0 8px 20px rgba(15,122,90,0.30)">'
            f'<a href="{H.escape(url)}" style="display:inline-block;box-sizing:border-box;text-align:center;padding:17px 44px;color:#ffffff;'
            f'font-weight:700;text-decoration:none;font-size:16px;line-height:1.3;letter-spacing:0.01em;border-radius:999px">{label}</a>'
            '</td></tr></table>'
            f'<div style="font-size:13px;color:{MUTED};margin-top:12px">{hint}</div>'
            '</td></tr></table>')

def icon(name, href, title):
    return (f'<td style="padding-right:8px"><a href="{H.escape(href)}" title="{title}" style="text-decoration:none">'
            f'<img src="{ICONS % name}" width="34" height="34" alt="{title}" style="display:block;border:0;width:34px;height:34px"></a></td>')

def signature():
    links = (icon("phone", f"tel:{PHONE_TEL}", PHONE)
             + icon("whatsapp", f"https://wa.me/{PHONE_TEL.lstrip('+')}", "WhatsApp")
             + icon("mail", f"mailto:{EMAIL}", EMAIL)
             + icon("globe", SITE, "givyx.com")
             + icon("instagram", INSTAGRAM, "Instagram")
             + icon("linkedin", LINKEDIN, "LinkedIn")
             + icon("pin", MAPS, "Karola Bunscha 15A, Kraków"))
    # Icons go under the logo/name row, not beside it: seven tiles plus the logo do not fit a phone.
    return (f'<hr style="border:0;border-top:1px solid {RULE};margin:26px 0 18px">'
            '<table role="presentation" cellspacing="0" cellpadding="0" style="width:auto"><tr>'
            f'<td style="vertical-align:top;padding-right:14px;width:64px"><a href="{SITE}"><img src="{LOGO}" width="64" height="64" alt="Givyx" '
            'style="display:block;border:0;width:64px;height:64px"></a></td>'
            '<td style="vertical-align:top">'
            '<p style="margin:0 0 2px;line-height:1.35"><strong style="font-size:16px">Stanisław Zakharevich</strong><br>'
            f'<span style="font-size:14px;color:{MUTED}">Director of Givyx</span></p>'
            f'<p style="margin:0;font-size:13px;line-height:1.5;color:{MUTED}">{TAGLINE}</p>'
            '</td></tr></table>'
            f'<table role="presentation" cellspacing="0" cellpadding="0" style="width:auto;margin-top:14px"><tr>{links}</tr></table>')

def p(t): return f"<p>{t}</p>"
def ul(items): return '<ul style="margin:6px 0 14px;padding-left:20px">' + "".join(f"<li style='margin:3px 0'>{i}</li>" for i in items) + "</ul>"

def main():
    n = json.load(open(sys.argv[1])); s = json.load(open(sys.argv[2]))
    name = H.escape(s["name"])
    url = f"{n['demo_url']}?utm_source=email&utm_medium=oferta&utm_campaign={n['campaign']}&utm_content={s['code']}"
    bare = re.sub(r"^https?://|/$", "", n["demo_url"])
    version = (f"Wersję dla {name} — z Waszą nazwą, usługami, zdjęciami i numerem — przygotujemy do obejrzenia zanim cokolwiek zapłacicie. "
               "Wystarczy odpisać „tak” albo nazwę firmy.")
    offer = ["249 zł/mies. — bez umowy, rezygnacja w każdej chwili",
             "Budowa strony gratis i pierwszy miesiąc gratis",
             "Uruchomienie na Waszej domenie w 2 dni"]
    offer_html = ["<strong>249 zł/mies.</strong> — bez umowy, rezygnacja w każdej chwili",
                  "<strong>Budowa strony gratis</strong> i <strong>pierwszy miesiąc gratis</strong>",
                  offer[2]]
    included = ["utrzymanie, zmiany i poprawki — piszecie, my robimy",
                "rozwój strony i nowe funkcje bez dopłat",
                "rezerwacja online i formularz kontaktowy — każde zgłoszenie od razu na Wasz e-mail",
                "e-maile do Waszych klientów (potwierdzenia, przypomnienia) — bez dopłat",
                "możliwość dodania SMS-ów do klientów",
                n["closing"]]
    contact = f"zadzwońcie do mnie na {PHONE} albo po prostu odpiszcie na tego maila — odpowiem tego samego dnia."

    body = (p("Dzień dobry,")
        + p(n["intro"])
        + cta(url, "Zobacz przykładową stronę&nbsp;→", f"{bare} · otwiera się na telefonie")
        + p(n["link_hint"])
        + p(version)
        + p("<strong>Oferta</strong>") + ul(offer_html)
        + p("<strong>W cenie</strong>") + ul(included)
        + p("<strong>Jak się skontaktować:</strong> " + contact.replace(PHONE, f'<a href="tel:{PHONE_TEL}" style="color:{ACCENT};font-weight:600">{PHONE}</a>'))
        + p("Pozdrawiam,")
        + signature())

    bullets = lambda items: "".join(f"- {i}\n" for i in items)
    text = (f"{n['title_prefix']} {s['name']}\n\nDzień dobry,\n\n{n['intro']}\n\n"
            f"Zobacz przykładową stronę: {url}\n{n['link_hint']}\n\n{H.unescape(version)}\n\n"
            f"Oferta\n{bullets(offer)}\nW cenie\n{bullets(included)}\n"
            f"Jak się skontaktować: {contact}\n\nPozdrawiam,\n\n--\nStanisław Zakharevich\nDirector of Givyx\n{TAGLINE}\n"
            f"{PHONE} (tel./WhatsApp) · {EMAIL} · givyx.com\n{INSTAGRAM} · {LINKEDIN}\nKarola Bunscha 15A, 30-392 Kraków\n")

    req = {"to": [s["to"]], "subject": n["subject"], "layout": "givyx", "locationId": "l_givyx",
           "eyebrow": "", "title": f"{n['title_prefix']} {name}", "badge": "Oferta",
           "replyTo": EMAIL, "showContact": False, "html": body, "text": text}
    print(json.dumps(req, ensure_ascii=False))

if __name__ == "__main__":
    main()
