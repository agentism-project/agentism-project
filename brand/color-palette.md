# Agentism Color Palette

**Status**: DRAFT — Awaiting community feedback per CC-017  
**Last updated**: 2026-03-06  
**Satisfies**: CC-039 (color palette with WCAG contrast), CC-042 (cultural neutrality)

---

## Primary Palette

The palette is derived from the symbol's existing colors, plus one accent color. Maximum 3 colors + black/white per CC-039.

| Role | Color | Hex | RGB | Usage |
|------|-------|-----|-----|-------|
| **Primary** | Near-black | `#111111` | 17, 17, 17 | Symbol fill, headings, body text |
| **Background** | White | `#FFFFFF` | 255, 255, 255 | Page backgrounds, symbol details |
| **Accent** | *To be selected* | *TBD* | *TBD* | Links, highlights, calls to action |

### Accent Color — Recommendation

The accent color must satisfy: culturally neutral (CC-042), warm but serious, not associated with existing political/tech brands.

**Selection deferred to community input.** Candidate directions based on SRS 6.8.4 constraints:

| Direction | Example Range | Rationale | Risk |
|-----------|---------------|-----------|------|
| Teal/deep cyan | `#0D7377` – `#1A9CA0` | Neutral across cultures, distinct from corporate blue, balances warmth and seriousness | Could feel "tech startup" if too bright |
| Warm amber | `#C4851C` – `#D4952C` | Human, organic, warm — counterbalances the geometric symbol | Could feel "luxury brand" |
| Muted coral | `#C05746` – `#D06756` | Warm, human, energetic without being aggressive | Proximity to red — review for political association |

## WCAG 2.1 AA Contrast Ratios

Minimum contrast ratio: **4.5:1** for normal text, **3:1** for large text (18px+ bold or 24px+ regular).

| Combination | Ratio | AA Normal | AA Large |
|-------------|-------|-----------|----------|
| `#111111` on `#FFFFFF` | **17.4:1** | PASS | PASS |
| `#FFFFFF` on `#111111` | **17.4:1** | PASS | PASS |

> Accent color contrast ratios will be calculated once the accent is selected.

## Colors to Avoid (per SRS 6.8.4)

| Color | Reason |
|-------|--------|
| Pure red (`#FF0000` vicinity) | Communist/socialist association |
| National flag combinations | Implies national allegiance (contradicts CP-005) |
| Facebook/LinkedIn blue (`#1877F2`, `#0A66C2`) | Too close to existing tech brands |
| Black + red combinations | Anarchist association |

## Usage Notes

- The primary palette is intentionally minimal. A two-tone (black/white) identity is the strongest foundation — an accent color adds warmth but is not required for the symbol itself.
- The symbol must never appear in the accent color alone — it is always `#111111` on light or `#FFFFFF` on dark.
- The accent color is reserved for UI elements (links, buttons, highlights), not for the symbol.
