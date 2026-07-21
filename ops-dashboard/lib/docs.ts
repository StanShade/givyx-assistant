/**
 * The read-only document registry.
 *
 * An allowlist, not a directory walk: the dashboard can only ever render files
 * named here, so a crafted slug cannot reach anything else in the checkout.
 */

export interface DocEntry {
  slug: string;
  title: string;
  /** Repo-relative path inside the data directory. */
  path: string;
  blurb: string;
}

export const DOCS: DocEntry[] = [
  { slug: "state", title: "STATE", path: "STATE.md", blurb: "Start here — single source of truth" },
  { slug: "log", title: "LOG", path: "LOG.md", blurb: "Every action and its effect" },
  { slug: "growth", title: "GROWTH", path: "GROWTH.md", blurb: "Goals + confirmed decisions" },
  { slug: "pipeline", title: "Pipeline", path: "prospects/pipeline.md", blurb: "Ranking + send log" },
  {
    slug: "prospects",
    title: "Prospects",
    path: "prospects/krakow-car-services.md",
    blurb: "29 researched Kraków car services",
  },
  {
    slug: "outreach",
    title: "Outreach",
    path: "outreach/wave1-messages.md",
    blurb: "Ready-to-send SMS per prospect",
  },
  { slug: "build", title: "Preview build", path: "previews/BUILD.md", blurb: "Preview build contract" },
  { slug: "readiness", title: "Readiness", path: "READINESS.md", blurb: "Go-live gut-check" },
];

export function findDoc(slug: string): DocEntry | undefined {
  return DOCS.find((d) => d.slug === slug);
}

/** Docs that get their own page rather than the generic viewer. */
export const NAV = [
  { href: "/", label: "Home" },
  { href: "/tasks", label: "Tasks" },
  { href: "/decisions", label: "Decisions" },
  { href: "/log", label: "Log" },
  { href: "/doc/state", label: "State" },
  { href: "/doc/pipeline", label: "Pipeline" },
  { href: "/doc/growth", label: "Growth" },
  { href: "/doc/prospects", label: "Prospects" },
  { href: "/doc/outreach", label: "Outreach" },
  { href: "/doc/build", label: "Build" },
];
