/**
 * Live plan catalog from api.givyx.com — the real current pricing, not a copy.
 *
 * Response shape (verified 2026-07-21):
 *   { data: [ { tier, displayName, highlight, aiAssistant, support,
 *               limits: {...}, features: { name: bool },
 *               prices: [ { id, currency, amountCents, interval, isDefault,
 *                           stripePriceId } ] } ], success: true }
 *
 * Read-only and non-essential: if the API is slow, down or changes shape the
 * home view says "unavailable" and renders everything else. Never throws.
 */

export interface PlanPrice {
  interval: string;
  currency: string;
  /** Major units (zł), derived from amountCents. */
  amount: number | null;
  stripePriceId: string | null;
  isDefault: boolean;
}

export interface PlanView {
  tier: string;
  name: string;
  highlight: boolean;
  aiAssistant: string | null;
  support: string | null;
  prices: PlanPrice[];
  features: { name: string; on: boolean }[];
  limits: { name: string; value: string }[];
}

export type PlansResult =
  | { ok: true; plans: PlanView[]; url: string }
  | { ok: false; reason: string; url: string };

const TIMEOUT_MS = 4000;

function str(value: unknown): string | null {
  return typeof value === "string" && value.trim() ? value.trim() : null;
}

function readPrices(raw: Record<string, unknown>): PlanPrice[] {
  const list = Array.isArray(raw.prices) ? raw.prices : [];
  return list.flatMap((entry) => {
    if (!entry || typeof entry !== "object") return [];
    const p = entry as Record<string, unknown>;
    const cents = typeof p.amountCents === "number" ? p.amountCents : null;
    return [
      {
        interval: str(p.interval) ?? "",
        currency: (str(p.currency) ?? "pln").toUpperCase(),
        amount: cents === null ? null : cents / 100,
        stripePriceId: str(p.stripePriceId),
        isDefault: p.isDefault === true,
      },
    ];
  });
}

function readFlags(value: unknown): { name: string; on: boolean }[] {
  if (!value || typeof value !== "object") return [];
  return Object.entries(value as Record<string, unknown>).map(([name, v]) => ({
    name,
    on: v === true,
  }));
}

function readLimits(value: unknown): { name: string; value: string }[] {
  if (!value || typeof value !== "object") return [];
  return Object.entries(value as Record<string, unknown>).map(([name, v]) => ({
    name,
    value: v === null || v === undefined ? "∞" : String(v),
  }));
}

function normalize(payload: unknown): PlanView[] {
  const root = payload && typeof payload === "object" ? (payload as Record<string, unknown>) : {};
  const list = Array.isArray(root.data)
    ? root.data
    : Array.isArray(root.plans)
      ? root.plans
      : Array.isArray(payload)
        ? payload
        : [];
  return list.flatMap((entry) => {
    if (!entry || typeof entry !== "object") return [];
    const raw = entry as Record<string, unknown>;
    const tier = str(raw.tier) ?? str(raw.key) ?? "";
    const name = str(raw.displayName) ?? str(raw.name) ?? tier;
    if (!name) return [];
    return [
      {
        tier: tier || name.toLowerCase(),
        name,
        highlight: raw.highlight === true,
        aiAssistant: str(raw.aiAssistant),
        support: str(raw.support),
        prices: readPrices(raw),
        features: readFlags(raw.features),
        limits: readLimits(raw.limits),
      },
    ];
  });
}

export async function fetchPlans(): Promise<PlansResult> {
  const url = process.env.OPS_PLANS_URL || "https://api.givyx.com/plans";
  try {
    const response = await fetch(url, {
      signal: AbortSignal.timeout(TIMEOUT_MS),
      headers: { accept: "application/json" },
      next: { revalidate: 300 },
    });
    if (!response.ok) return { ok: false, reason: `HTTP ${response.status}`, url };
    const plans = normalize(await response.json());
    if (plans.length === 0) return { ok: false, reason: "no plans in the response", url };
    return { ok: true, plans, url };
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    return { ok: false, reason: /timed?\s?out|abort/i.test(message) ? "timed out" : message, url };
  }
}

export function formatPrice(price: PlanPrice): string {
  if (price.amount === null) return "—";
  const symbol = price.currency === "PLN" ? "zł" : price.currency;
  const amount = Number.isInteger(price.amount)
    ? String(price.amount)
    : price.amount.toFixed(2).replace(".", ",");
  return `${amount} ${symbol}`;
}
