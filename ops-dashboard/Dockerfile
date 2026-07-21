# syntax=docker.io/docker/dockerfile:1

FROM node:22-alpine AS base

FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci

FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM base AS runner
WORKDIR /app

# git is a runtime dependency, not a build one: every write the dashboard makes
# is committed to the mounted data repo so there is always an undo.
#
# openssh-client is NOT pulled in by the git package on Alpine, and without it
# git cannot use the SSH transport at all: commits land locally and every push
# fails with "make sure you have the correct access rights". Verified in prod
# 2026-07-21 — the container had no /usr/bin/ssh.
RUN apk add --no-cache git wget openssh-client

ENV NODE_ENV=production

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

# The operating memory is mounted here, read-write, and must be a git checkout.
ENV OPS_DATA_DIR=/data
VOLUME ["/data"]

EXPOSE 3010
ENV PORT=3010
ENV HOSTNAME="0.0.0.0"

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s \
  CMD wget -q -O /dev/null http://127.0.0.1:3010/login || exit 1

CMD ["node", "server.js"]
