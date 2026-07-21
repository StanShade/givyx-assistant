# Ops/Deploy audit — raw findings (2026-07-18)

Architecture: ONE 4vCPU/8GB kylos.pl VPS (83.168.71.126), 10 Docker containers behind Caddy.
Tenant data in Azure Table Storage + Redis + Qdrant; analytics Postgres + tenant images on VPS disk.

## Findings
1. P1 reliability L — Single VPS = total SPOF. No LB/failover. Box dies → everything down, ~1h manual RTO.
2. **P0 backup M — No off-box backups.** Weekly cron backs up only caddy_data (certs) to SAME disk. Images + analytics DB not backed up. Disk loss = unrecoverable.
3. P1 backup S — Tenant images live ONLY on VPS since 2026-06-12, no backup (Azure has passive pre-flip copy only).
4. P1 backup S — Analytics Postgres (givyx-db) has no pg_dump/backup. All visitor history one disk-loss from gone.
5. P1 scaling L — Custom-domain provisioning fully manual: new Caddy block + container + env + SSH key + GH secret + deploy branch per domain. No on-demand TLS/catch-all. Hard scaling ceiling.
6. P1 scaling M — Per-domain = per-container; NO resource limits on any container (8GB shared). Custom-domain container-per-tenant exhausts RAM before 50 tenants.
7. **P0 monitoring M — No uptime/error/lead-failure monitoring.** Only Beszel host CPU/RAM. No per-site uptime, no HTTP error alert, no lead-email-failure alert. Outages silent until client complains.
8. P1 security L — Live secrets committed to git (env/*.env: JwtSecret, CryptoSecret, Azure/Redis/Qdrant conn, SendGrid, Google OAuth x4, GoDaddy DNS, Postgres pw). Repo privacy is only protection.
9. P2 security S — metrics.givyx.com has no Caddy basic_auth/security headers (only Beszel's own login). Docs diverged from reality.
10. P1 reliability S — apply-ops.sh does NOT auto-rollback env on healthcheck failure (deploy.sh does for images). One typo → service down until human fixes.
11. P1 ci-cd M — Deploy pipeline flakes on SSH/runner step, needs manual reruns; kylos anti-DDoS rate-limits rapid SSH.
12. P1 ci-cd M — No staging env, no test gate before prod. Push to main → straight to single prod box.
13. P1 reliability L — Single-replica services → every deploy = brief downtime; MCP long-lived SSE breaks on restart (cold-start wedge).
14. P2 reliability S — Wildcard TLS depends on ONE GoDaddy API credential; lapse = all *.givyx.com cert renewals fail.
15. P2 tech-debt S — rollback.sh + manual-rollback.yml don't cover custom-domain container (givyx-ipr, the real paying tenant).
16. P1 scaling M — 32K Azure Table page ceiling; MCP write fails but reports SUCCESS (silent content loss). Each locale ~25% tax.
17. P2 automation M — Publish Preview→Production manual + blocked for agents; no MCP location/slug-create tool.
18. P2 monitoring S — Custom-domain onboarding: no DNS/cert-readiness check; client DNS typo → indefinitely broken www, no alert.
19. P2 ci-cd S — Branch sprawl; ops checkout not on main. Obscures what's deployed.
20. P2 security M — Containers run as root; docker.sock mounted into beszel-agent. Wider RCE blast radius (one traversal bug already found).

## Summary
Pipeline is functional + thoughtfully scripted, but rests on ONE un-redundant VPS with no off-box
backups and near-zero monitoring. Scaling to 10-50 blocked by manual per-custom-domain infra + no
resource limits + 32K ceiling. Biggest risks are SILENT (site 500, lead-email fail, stuck cert, dropped write).
TOP FIX: external monitoring + alerting (uptime, HTTP errors, lead-email failure). Runner-up: off-box nightly backups (images + pg_dump + caddy_data).
