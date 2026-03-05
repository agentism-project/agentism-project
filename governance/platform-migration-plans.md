# Platform Migration Plans

**Layer**: Durable (Layer 2)
**Version**: 0.1.0
**Status**: DRAFT

This document maintains documented migration paths for all platforms used by the Agentism project. Per CP-004 and NFR-003, the project must not create platform lock-in that prevents migration.

---

## Migration Principles

1. **Content is always exportable** — All content is stored as markdown in Git. Changing platforms does not lose content.
2. **30-day notice before migration** — Any platform change requires 30-day public notice.
3. **No single-point-of-failure** — Critical functions must have at least one fallback.
4. **Community notification** — Contributors are notified through all active channels before migration.

---

## GitHub → Alternative Version Control

**Trigger**: GitHub becomes unavailable, policy-hostile, or loses community trust.

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Export full repository as `.tar.gz` | Core Maintainer |
| 2 | Push mirror to GitLab.com and/or Codeberg.org | Core Maintainer |
| 3 | Update all internal links and README to point to new primary | Core Maintainer |
| 4 | Redirect GitHub repository README with migration notice (if still accessible) | Core Maintainer |
| 5 | Update `content/official-channels.md` | Core Maintainer |
| 6 | Announce migration through email list and all active channels | Core Maintainer |

**Fallback hosts** (in order of preference):
1. Codeberg.org — not-for-profit, EU-based, GDPR-compliant
2. GitLab.com — commercial but open-source core, self-hostable
3. Self-hosted Gitea — full control, requires infrastructure team

**Data format**: All content is markdown + Git history. Portable to any Git host without transformation.

---

## GitHub Discussions → Alternative Forum

**Trigger**: GitHub Discussions becomes unusable or discontinuation announced.

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Export all discussions (GitHub API export or third-party tool) | Core Maintainer |
| 2 | Stand up Discourse instance (self-hosted or hosted) | Technology WG |
| 3 | Import exported content where format allows | Technology WG |
| 4 | Announce migration with link to new forum | Core Maintainer |
| 5 | Keep GitHub Discussions readable (but not writable) for 90 days post-migration | Core Maintainer |

**Data format**: GitHub Discussions exports via API to JSON. Discourse import requires transformation. Some formatting loss expected — post content preserved.

---

## GitHub Pages → Alternative Hosting

**Trigger**: GitHub Pages becomes unavailable or the project migrates primary version control.

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Hugo build runs locally: `cd website && hugo --minify` | Core Maintainer |
| 2 | Upload `website/public/` to Netlify, Cloudflare Pages, or self-hosted | Technology WG |
| 3 | Update DNS if custom domain | Core Maintainer |
| 4 | Rebuild deploy workflow for new host | Technology WG |

**Fallback hosts** (in order of preference):
1. Cloudflare Pages — generous free tier, global CDN
2. Netlify — established, generous free tier
3. Self-hosted nginx — full control, requires infrastructure

---

## Open Collective → Alternative Funding Platform

**Trigger**: Open Collective discontinues service or becomes policy-hostile.

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Export donor history and transaction records (PDF and CSV) | Founder / Treasurer |
| 2 | Publish archived financial records in `governance/financial-archives/` | Founder / Treasurer |
| 3 | Set up alternative (Ko-fi, Liberapay, or direct bank transfer) | Founder |
| 4 | Notify all current donors 30 days in advance | Founder |
| 5 | Update `content/official-channels.md` | Core Maintainer |

**Alternatives** (in order of preference):
1. Liberapay — non-profit, no platform fees
2. Ko-fi — simple, low fees
3. Direct bank transfer with quarterly public reporting — maximum transparency, some friction

---

## Review Schedule

This document is reviewed annually as part of the Durable-tier document review cycle. Last reviewed: 2026-03-05.

---

*This document was co-developed with an AI Collaborator (Claude Sonnet 4.6 via GitHub Copilot). Reviewed and approved by the Founder. Per CP-004 and HAI-001.*

