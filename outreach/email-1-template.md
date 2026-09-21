# Email 1 — look v4.1 (2026-09-21, Stan's OK) on top of copy v3

Shared parts in `ops/tools/email_parts.py` (both builders import it): header **pill** "Oferta"/"Offer" beside the
logo · pill CTA + bare demo host caption · signature under a rule — rounded Givyx tile, **name/title/tagline by
language** (PL Stanisław Zakharevich · Dyrektor, Givyx · Strony internetowe i aplikacje mobilne · EN Stan
Zakharevich · Director, Givyx · Websites & mobile apps · RU Слава Захаревич · Директор, Givyx · Сайты и мобильные
приложения), 7 icon links (phone, WhatsApp, mail, site, Instagram `givyx.ai`, LinkedIn `company/givyx`, map) ·
shell contact block off (`showContact:false`) · `text` part on every send. US mails keep the CAN-SPAM line with the
postal address in words. Preview: `previews/email-v4.1-warsztat.html`. Generic variant: `build-email-v4.py`.

# Email 1 — v3 (2026-09-15, Stan's second round; supersedes everything below)

Stan's rules: **never mention Google reviews/ratings in the email** (the rating stays on the site, not in the
copy) · **open with a hook about their customers** that pulls them to the example, button right under it ·
**explicit contact line**: call 571 088 012 or just reply to this mail; number in the signature too.
Structure: hook → button → who I am + `fakt` + "Na stronie jest {na_stronie}" → `dlaczego` → Oferta →
W cenie → Jak się skontaktować → signature. Spec fields: `hook`, `fakt`, `na_stronie`, `dlaczego`.

# Email 1 — v2 (2026-09-15, Stan's brief; superseded by v3 above)

**Offer changed:** one price — **249 zł/mies.**, no contract, cancel any time, **site built free, first month
free**. The 149/249/750 ladder is no longer in the email. Benefits listed as "W cenie": maintenance, changes
and fixes · further development and new features at no extra cost · online booking + contact form, every
submission straight to their e-mail · e-mails to their customers (confirmations, reminders) at no extra cost ·
option to add SMS to customers · works on the phone. Tone: professional offer, warm, personal.

**Personal to each prospect — three fields, all from the research pack + the clone log:**
`fakt` (what they do well, verified) · `na_stronie` (exactly what we put on their site: services, prices if
quoted, photos used, rating, hours/booking) · `dlaczego` (1–2 sentences why the site matters for *them*).

Builder: `ops/tools/build-email-v2.py spec.json` — specs per prospect in `outreach/batch4-specs/<slug>.json`.
Subject: `Strona dla {{NAZWA}} — podgląd i oferta`. Send: `ops/tools/send-one.sh`, one prospect per call.

> Dzień dobry,
>
> Z tej strony Stan z Givyx, z Krakowa. Zanim napisałem, sprawdziłem, jak pracujecie: {{fakt}}.
>
> Przygotowaliśmy wersję strony dla {{NAZWA}}: {{na_stronie}}.
>
> **[Zobacz stronę →]({{URL}})**
>
> {{dlaczego}}
>
> **Oferta**
> - **249 zł/mies.** — bez umowy, rezygnacja w każdej chwili
> - **Budowa strony gratis** i **pierwszy miesiąc gratis**
> - Uruchomienie na Waszej domenie w 2 dni
>
> **W cenie**
> - utrzymanie, zmiany i poprawki — piszecie, my robimy
> - rozwój strony i nowe funkcje bez dopłat
> - rezerwacja online i formularz kontaktowy — każde zgłoszenie od razu na Wasz e-mail
> - e-maile do Waszych klientów (potwierdzenia, przypomnienia) — bez dopłat
> - możliwość dodania SMS-ów do klientów
> - strona działa na telefonie; my dbamy o stronę, Wy o auta
>
> Jeśli coś ma wyglądać inaczej — usługi, ceny, zdjęcia — odpiszcie, dopasuję. Albo zadzwońcie.
>
> Pozdrawiam,
> Stan
> Givyx

---

# Email 1 — the "we built a version for you" offer · template (PL + EN)

Reconstructed 2026-09-14 from the rules Stan set on 09-10/09-11 (the sent bodies were composed
inline and not saved). **Stan re-approves this once; then every batch reuses it verbatim** with
only `{{…}}` filled. Rules baked in: warm, not official · lead with a verified fact about what they
do WELL, never a fault list · describe the experience, invite the click · 149/249/750 shown the
same way every time · one send per curl · goes to Stan first.

Send call: `POST /emails` with `layout:"givyx"`, `locationId:"l_givyx"` (footer = Givyx address,
phone, email — never in the body), `replyTo: info@givyx.com`, unique `utm_content`.

## PL

**Subject:** `Zbudowaliśmy wersję strony dla {{NAZWA}}`
**Eyebrow:** `Oferta` · **Title:** `Strona dla {{NAZWA}}`

> Dzień dobry,
>
> Z tej strony Stan z Givyx, z Krakowa. Zanim napisałem, sprawdziłem Was: {{FAKT}}.
>
> Zbudowaliśmy wersję Waszej strony — z Waszą nazwą, telefonem, usługami i oceną z Google:
>
> **[Zobacz stronę →]({{URL}})**
>
> Strona zaczyna się od wjazdu do hali i zjazdu pod maskę silnika, potem usługi na pierścieniu,
> rezerwacja wizyty i kontakt — wszystko działa na telefonie. Zobaczcie sami, to 30 sekund.
>
> Jeśli się podoba, uruchamiamy ją na Waszej domenie w 2 dni. Abonament:
> **149 zł/mies.** — ta strona, jak w podglądzie · **249 zł/mies.** — rozbudowana, nowoczesna,
> z rezerwacją online · **750 zł/mies.** — płatności online, bez brandingu Givyx.
> Utrzymanie, zmiany i poprawki są w cenie — my dbamy o stronę, Wy o auta.
> **Bez umowy, rezygnacja w każdej chwili, pierwszy miesiąc gratis.**
>
> Odpiszcie na tego maila albo zadzwońcie — chętnie dopasuję stronę pod Was.
>
> Pozdrawiam,
> Stan

`{{URL}}` = `https://{{slug}}.givyx.com/?utm_source=email&utm_medium=oferta&utm_campaign={{slug}}&utm_content={{code}}`

## EN (US)

**Subject:** `We built a version of your site — {{NAME}}`
**Eyebrow:** `Offer` · **Title:** `A site for {{NAME}}`

> Hi,
>
> Stan here, from Givyx. Before writing I looked you up: {{FACT}}.
>
> We built a version of your site — your name, phone, services and reviews:
>
> **[See the site →]({{URL}})**
>
> It opens with a drive into the shop and a dive under the hood, then your services, online
> booking and contact — all on the phone. Takes 30 seconds to look.
>
> If you like it, it goes live on your own domain in 2 days. **$49/month**, maintenance and changes
> included — we keep the site current, you keep fixing cars. **No contract, cancel any time, first month free.**
>
> Reply to this email or call — happy to adjust anything.
>
> Stan
>
> This is an advertisement. Reply "unsubscribe" and you won't hear from me again.

`{{URL}}` = `https://{{slug}}.givyx.com/?utm_source=email&utm_medium=offer&utm_campaign={{slug}}&utm_content={{code}}`

## Risk reversal — DECIDED 2026-09-14 (Stan)
No contract, cancel any time, **first month free** for the first clients. The line above is now part of
both templates. The 30 emails sent through 09-14 did not carry it; every D+5 follow-up does.
