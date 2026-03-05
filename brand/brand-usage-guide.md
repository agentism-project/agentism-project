# Agentism Brand Usage Guide

**Status**: DRAFT — Awaiting community feedback per CC-017  
**Last updated**: 2026-03-06  
**Satisfies**: CC-045 (brand usage guide), CC-044 (format requirements)

---

## The Symbol

The Agentism symbol represents the synthesis of autonomous agents and human flourishing. It consists of four elements within a unified form:

1. **Base shape** — Semicircular left side (organic, human) fused with angular right side (structured, agent)
2. **S-curve** — Flowing line representing circulation of prosperity, connecting both sides
3. **Circle** (left) — The human eye, organic form, representing human agency
4. **Diamond** (right) — The agent eye, geometric form, representing structured precision

### Symbol Anatomy

```
         S-curve (prosperity flow)
            ╱
    ┌──────/──────────────┐
    │   ╱                 │
    │ ●         ◇         │
    │ circle    diamond   │
    │ (human)   (agent)   │
    │                     │
    └─────────────────────┘
    ╰─── organic ───╯╰ angular ╯
         (left)       (right)
```

## Correct Usage

### Approved Variants

| Variant | File | Use Case |
|---------|------|----------|
| Primary | `agentism-symbol.svg` | Default — light backgrounds |
| Monochrome | `agentism-symbol-monochrome.svg` | Single-color printing, stamps |
| Inverted | `agentism-symbol-inverted.svg` | Dark backgrounds |
| Favicon | `agentism-favicon.svg` | Browser tabs, app icons |

### Minimum Size

- **Digital**: 32px height minimum for general use. At 16px (favicon), use `agentism-favicon.svg`.
- **Print**: 10mm height minimum.

### Clear Space

Maintain clear space around the symbol equal to the height of the diamond element (~56px at full scale, or ~14% of total height). No text, images, or other graphic elements should intrude into this clear space.

```
    ┌─────────────────────────────┐
    │         clear space         │
    │   ┌─────────────────────┐   │
    │   │                     │   │
    │   │      [SYMBOL]       │   │
    │   │                     │   │
    │   └─────────────────────┘   │
    │         clear space         │
    └─────────────────────────────┘
```

### Color Rules

- **On light backgrounds**: Use primary variant (`#111111` fill)
- **On dark backgrounds**: Use inverted variant (`#FFFFFF` fill)
- **Single-color contexts**: Use monochrome variant
- The symbol must never appear in the accent color — it is always near-black or white

### Backgrounds

The symbol works on:
- White or light neutral backgrounds (preferred)
- Dark backgrounds using the inverted variant
- Solid color backgrounds where sufficient contrast exists (minimum 4.5:1 ratio)

## Incorrect Usage — Prohibited Modifications

| Prohibited | Reason |
|-----------|--------|
| Stretching or distorting proportions | Breaks the visual balance between organic and geometric |
| Rotating the symbol | The orientation is part of the meaning (human left, agent right) |
| Adding drop shadows, gradients, or 3D effects | Contradicts the flat, printable design principle |
| Placing on busy or low-contrast backgrounds | Reduces legibility |
| Using partial elements of the symbol in isolation | The four elements are a unified composition |
| Adding text inside or overlapping the symbol | Clutters the clear, minimal form |
| Recoloring the internal details (S-curve, eyes) | The white internal details are structural, not decorative |
| Outlining instead of filling the base shape | Changes the symbol's visual weight and identity |

## File Formats

### Source of Truth

The SVG files in `brand/` are the authoritative source. All other formats are derived from these.

### PNG Export Sizes (CC-044)

Export from SVG at these standard sizes (square, with equal padding on all sides):

| Size | Use Case |
|------|----------|
| 16×16px | Favicon (legacy browsers) |
| 32×32px | Favicon (standard), small UI elements |
| 64×64px | App icon (small) |
| 128×128px | App icon (medium), document headers |
| 256×256px | Social media profile image |
| 512×512px | Open Graph image, presentation slides |
| 1024×1024px | Print, large-format, maximum quality |

**Export instructions**: Open any SVG file in a vector editor (Inkscape, Figma, Illustrator) and export as PNG at the target size. Maintain transparent background for monochrome and inverted variants; use white background for the primary variant.

## With Text (Wordmark)

When the symbol appears alongside the project name:

- The word "agentism" appears to the right of the symbol, not below
- Use lowercase "agentism" — the project name is never capitalized except at the start of a sentence
- Minimum spacing between symbol and text: equal to the clear space
- Font: see typography selection (CC-040, pending)

## License

All brand assets are licensed under [CC BY-SA 4.0](../LICENSE-docs). Trademark restrictions on the name and symbol still apply — see [TRADEMARK.md](../TRADEMARK.md).
