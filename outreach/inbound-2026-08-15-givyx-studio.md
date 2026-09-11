# Inbound lead — 2026-08-15 — Givyx Studio

**First inbound contact-form lead.** Status: draft written, **not sent** — awaiting Stan's OK.

## The record as received

| Field | Value |
|---|---|
| Plan | `givyx-studio` |
| Email | fathan.arshaka911@gmail.com |
| Source page | `/contact` |
| Campaign | Direct |
| Submitted | 15 Aug, 12:08 (2 days before this draft) |
| Browser | `node` |

No name, no message, no phone — the submission carries only the plan and the email.

## What `givyx-studio` actually means (verified on the live site)

Fetched `givyx.com/pricing` and `givyx.com/contact` on 2026-08-17:

- The four self-serve plans link to `/contact?plan=free|starter|studio|scale`.
- `?plan=givyx-studio` is used by **one** CTA only: *"Talk to the studio →"* in the
  *"Rather have it done for you? Meet Givyx Studio"* block — "Skip the builder entirely… fully custom
  professional site — designed, launched and maintained for you on a subscription", bullets
  *100% custom design & copy · Built & maintained by us · Unlimited change requests*,
  priced *"Custom quote · no commitment"*.
- So this person read the pricing page and clicked the **done-for-you** option, not the $49/mo tier.

Published USD anchors on that page (the only prices we may quote): Free $0 · Starter $29 · Studio $49 ·
Scale $199 per month; à la carte custom design **from $600**, full redesign **from $1,200**,
custom feature/integration from $400, logo & brand kit from $500.

**Do not quote 149/249/750 zł here** — that ladder is the Polish car-service offer, a different market.
Studio is quoted per project, so the reply's job is to gather enough to quote.

## Draft reply — EN (v3, per Stan: keep the first email short — apologise, ask what site, promise variants)

**To:** fathan.arshaka911@gmail.com
**Reply-to:** stan.zak.inf@gmail.com
**Subject:** Sorry for the slow reply — what kind of site do you need?

> Hi Fathan,
>
> Sorry for the slow reply — your message came in on 15 August and it shouldn't have taken us this long.
>
> What kind of site do you need? Tell me a bit about the project: what it's for, roughly what should be
> on it, and anything you already have — domain, logo, text, photos.
>
> Once I know that, we'll quickly prepare a few variants for you to look at, and we'll take it from there.
>
> Best,
> Stan

*(Signature is just "Stan" — the branded `layout:givyx` footer already prints the Givyx name, address,
phone and info@givyx.com from the `l_givyx` location record, so repeating it in the body is noise.)*

## 🔴 Send BLOCKED — SendGrid is out of credits (2026-08-17)

Verification copy to `stan.zak.inf@gmail.com` attempted via `POST /emails`
(`layout:givyx`, `locationId:l_givyx`, replyTo Stan). Result:

```
sent 0 / failed 1
SendGrid send failed with status 401: {"errors":[{"message":"Maximum credits exceeded"}]}
```

**Givyx cannot send any email at all right now** — not this draft, not the prospect reply, and not the
automated lead notifications. Plausibly why this lead sat unseen for two days: the notification for it
may have failed the same way. Needs Stan to check the SendGrid account (plan limit vs. exhausted
credits); my attempt to query the SendGrid API for the plan/quota was blocked by the tool classifier.

## Manual send version (paste into Gmail while SendGrid is down)

**To:** `fathan.arshaka911@gmail.com`
**Subject:** `Sorry for the slow reply — what kind of site do you need?`

```
Hi Fathan,

Sorry for the slow reply — your message came in on 15 August and it shouldn't have taken us this long.

What kind of site do you need? Tell me a bit about the project: what it's for, roughly what should be
on it, and anything you already have — domain, logo, text, photos.

Once I know that, we'll quickly prepare a few variants for you to look at, and we'll take it from there.

Best,
Stan

—
Givyx
info@givyx.com · +48 571 088 012
givyx.com
```

The signature block is added **only** for the manual send. The API version drops it, because
`layout:"givyx"` renders name / address / phone / email from the `l_givyx` location record already.

**Send it from `info@givyx.com` if Gmail has that as a send-as identity** — he wrote to Givyx, so a
reply from a personal Gmail is a small trust wobble. If send-as isn't set up, your own Gmail is fine
and arguably warmer; just keep the signature so the company is identifiable. Either way a plain-text
Gmail reply beats the branded template here: it's a first human reply, not a notification.

## Notes for Stan before sending

- **The one commitment here is "a few variants."** When he replies, that's the personalised-preview
  play again — same as Speed-Gum and Intra Cars, but in English and with no business to research yet.
- **No prices, no plan explanation.** Both held back for the second email, once we know what he wants.
  The pricing anchors are recorded above if you want them later.
- **"Fathan" is inferred from the address**, not stated. Swap to "Hi there," if you'd rather not guess.
- **Language:** English. The site is EN-first with USD pricing, and the contact isn't Polish. PL/RU
  versions are easy if you want them.
- **`Browser: node`** — worth one check, not an alarm. If the contact form posts through a Next.js API
  route, the backend sees node's fetch and *every* submission will read `node`. If other submissions
  show real browsers and only this one says `node`, treat it as a scripted submission and don't invest
  a call in it. Free Gmail + no message is consistent with either reading.
- **Product gap this exposes:** `/contact` promises "Tell us what you're making", but the stored lead has
  no name and no message. Every inbound lead will need this round-trip until the form captures a name
  and a "what are you building" field.
- **The 1-day promise was missed** (2 days). Worth wiring the lead notification somewhere you actually see.
