# SendGrid compliance review — reply draft (ticket #29038472)

Received 2026-08-17 01:01 PDT. Reply to the ticket email so it threads; keep the number in the subject.

**Before sending, fill the four `[...]` placeholders.** I can't verify any of them and must not guess:
legal business name, NIP, the public profile URL, and which sample file gets attached.

**Subject:** `Re: Ticket #29038472 — account upgrade review — Givyx (givyx.com)`

---

> Hello,
>
> Thank you for reviewing the account. Answers to each of your questions below, in order.
>
> **1. Official website**
>
> https://givyx.com — live, and the sending domain for this account.
>
> **2. Business model, products and services**
>
> Givyx is a website platform for small businesses, based in Kraków, Poland. Customers get a hosted
> website on a monthly subscription: we design and build the site, host it, and maintain it for them.
> Plans run from a free single-page site up to larger multi-page sites, plus a done-for-you option
> where we build the site to the customer's brief. Public pricing is at https://givyx.com/pricing.
>
> Our customers are small local businesses — car service centres, trade services and similar — in
> Poland and Slovakia. The business operates as [LEGAL BUSINESS NAME / registered form], registered in
> Poland, NIP [NIP], at Karola Bunscha 15A, 30-392 Kraków, Poland.
>
> **3. Name and affiliation**
>
> [FULL LEGAL NAME], founder and owner of Givyx. Publicly verifiable at [LINKEDIN URL — or the CEIDG /
> Aleo register entry, which publicly lists the business name, owner, NIP and registered address].
>
> **4. Type of email: transactional, not marketing**
>
> All mail from this account is transactional and triggered by a specific action from a specific
> person. There is no mailing list, no campaign tooling, and no bulk send capability in our software.
> Concretely, the complete set of message types our platform can produce is:
>
> - Contact-form and enquiry notifications sent to the business owner whose own website received the
>   submission
> - Automated replies to the person who submitted that form
> - Booking requests and booking confirmations
> - Account email: password reset, email address verification, one-time codes, team invitations
> - Billing: subscription and payment notifications to paying customers
> - Operational alerts sent to our own address (uptime and backup monitoring)
> - Individual replies written by me to people who contacted us first
>
> Recipients are in every case either our own paying customers, someone who submitted a form on a
> website we host, or ourselves. We do not send marketing campaigns, newsletters, promotional blasts
> or announcements, and we have never used a purchased, rented or scraped list. Because there is no
> marketing mail, there is no opt-in page to link.
>
> **5. Content sample**
>
> Attached: [SAMPLE FILE]. Our privacy policy is published at https://givyx.com/privacy, and our
> physical mailing address (Karola Bunscha 15A, 30-392 Kraków, Poland) appears in the footer of every
> message we send, as the sample shows.
>
> **6. Volume and authentication**
>
> Expected volume is in the tens of messages per day, not thousands — it scales with our customer
> count, and we are an early-stage business. The sending domain is authenticated: DKIM is in place via
> your CNAMEs (`s1`/`s2._domainkey.givyx.com`), and we publish DMARC at `p=quarantine`. Click and open
> tracking are disabled on our sends.
>
> Happy to provide anything further, or to do a call if that is quicker.
>
> Best regards,
> [FULL LEGAL NAME]
> Givyx · givyx.com · info@givyx.com

---

## What to attach as the sample

Best option is a genuine transactional message, since that is what we told them we send. Candidates
that exist in `Givyx.Emailing/Templates/`: `ContactSubmissionLayout`, `FormResponseLayout`,
`BookingRequestLayout`, `PasswordResetLayout`, `VerifyEmailLayout`, `ProjectInquiryOtpLayout`,
`InviteLayout`, `FeedbackLayout`, `BookingConfirmationLayout`.

None are currently rendered to a file. Two ways to get one:

1. **Fastest:** attach `outreach/inbound-2026-08-15-givyx-studio-paste.html` — a real reply to someone
   who contacted us, showing the branded shell, the physical address in the footer and no marketing
   content. Accurate, but it is a sales reply rather than a system notification.
2. **Better:** render a contact-form notification and a password reset from the templates and attach
   both. That is precisely what the account sends most of, and it makes the "transactional" claim
   self-evident. Ask me and I'll produce them.

## 🔴 Decide this before replying: cold outreach and the AUP

The answer above says we send no unsolicited mail. **That is true of the platform, but not of what we
did in July**: offer emails went to Speed-Gum and Intra Cars, neither of whom had contacted us first.
Both were sent through this SendGrid account.

Telling a compliance reviewer "transactional only" and then resuming cold outreach on the same account
is how accounts get suspended after approval — a far worse outcome than the current delay. So pick one
and hold to it:

- **Recommended: keep SendGrid transactional-only.** Platform mail, billing, and replies to people who
  contacted us first. Cold prospecting continues the way it already works best for us anyway — SMS from
  Stan's phone, then a call, with any follow-up email sent by hand from a personal mailbox. Costs us
  nothing: the July emails produced no replies, while the phone did.
- **Or declare it honestly**: describe the outreach as low-volume manual B2B email to businesses whose
  contact details are published, sent one at a time. Reviewers may accept that, but it invites scrutiny
  and probably slows the ticket.

Note also that the answer's claim "the footer carries our physical address" is only true for the
branded `layout:"givyx"` shell. Ops alerts sent by `scripts/lib-alert.sh` are raw plain text to our own
address — worth mentioning only if they ask, since self-addressed monitoring is not what the rule targets.
