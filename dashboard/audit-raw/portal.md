# Portal audit — raw findings (2026-07-18)

Next.js 16, HeroUI v3. Redesign PRs #52-56 + API follow-ups #1-5 already SHIPPED (that doc is stale).
Nav (config/navigation.ts) is CLEAN — role/offering-gated, all hrefs real, honest empty-states.
Working & verified: web editor Deploy, Offering, Forms builder/preview/submissions, Analytics,
structured address, MCP token list/revoke, logo uploader, slug-availability, Stripe checkout/portal.

## P0 — blocks paying clients
1. broken-flow M — Mobile "Deploy to All Users" is a NO-OP (mobile-controls.tsx:43 onConfirm={()=>{}}). Mobile app can never publish.
2. broken-flow S — Mobile editor corner-radius inputs inert (border-editor.tsx:72-107 onChange={()=>{}}).
3. broken-flow M — Mobile editor style-variant picker does nothing (element-style-selector.tsx:60 console.log todo).

## P1 — important
4. redesign M — TWO conflicting billing flows on Manage plan: mailto "Request upgrade" (upgrade-modal→/feedback) vs real Stripe checkout (manage-plan.tsx:428+). Contradictory pay UX.
5. bug S — Checkout/portal errors use alert() not toast (manage-plan.tsx:170,186).
6. missing-feature L — "Billing & invoices" is Coming-soon stub (manage-plan.tsx:461). No invoice history.
7. unimplemented L — Account Settings mostly Coming-soon: password change, 2FA, sessions, notifications, export data, delete account. Only profile/theme/sign-in-list real. GDPR gap.
8. bug S — "Sign in with Google" mislabeled "Coming soon" but it's fully wired (login-form.tsx:144, auth.ts:125).
9. hidden-menu M — Mobile live-preview column built but hidden in prod (NEXT_PUBLIC_MOBILE_PREVIEW_URL unset; only shade.expo.app demo). No client sees mobile preview.
10. missing-feature M — Web editor "N unpublished changes" counter not implemented. Clients can't tell if they have undeployed edits.

## P2 — polish / tech-debt
11. missing-feature M — Web editor "Site structure" map missing (chat-component-preview.tsx).
12. missing-feature L — Home dashboard activity feed absent (needs events endpoint).
13. missing-feature M — Home "Top products" view counts absent (needs per-product analytics).
14. bug S — Table rows-per-page control inert (s-table.tsx:234 onRowsPerPageChange={()=>{}}).
15. improve M — Plan-list drag-to-reorder not implemented (plans-manager.tsx).
16. tech-debt S — Dead file components/user/login-form2.tsx (imported nowhere).
17. tech-debt S — Empty a11y key handlers (editable-text.tsx:63, sortable.tsx:49, component-button.tsx:47).
18. tech-debt S — Legacy no-op logo route (app/api/users/logo/route.ts:12).
19. improve S — Sidebar plan usage gauge shows label only, no bar.
20. redesign L — Mobile editor not at design fidelity (3-col layout). Least-finished surface (combine w/ 1-3).
21. improve S — Analytics polish: tooltips, donut, legend order (Sessions should lead).
22. redesign M — HeroUI Tabs/Drawer not pixel-matched (location-settings tabs, help drawer).

## Summary
~80% client-ready. Public/auth/home/analytics/offering/forms/team/location-settings shipped & functional —
a workshop client CAN log in, edit site, manage catalog/forms/team, see real analytics. Two soft spots
bite paying clients: MOBILE EDITOR (deploy no-op + dead controls, #1-3) and BILLING (contradictory upgrade
flows, alert() errors, no invoices, #4-6), plus thin Account Settings (#7). Close mobile-editor wiring +
settle billing UX before onboarding paying workshops.
