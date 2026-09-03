---
name: Gestión de redes de datos — SENA 228183
description: Señalética institucional colombiana en clave clara: paneles de fase autorables, numerales a escala de señal y un solo control de búsqueda.
colors:
  verde: "#39a900"
  verde-texto: "#2e7d00"
  amarillo: "#fdc300"
  sobre-verde: "#08210b"
  sobre-amarillo: "#22190a"
  sobre-amarillo-suave: "#5c4a08"
  papel: "#f2f5f1"
  panel: "#ffffff"
  ink: "#0a1710"
  ink-medio: "#405146"
  ink-tenue: "#566a5e"
  filete: "#cbd4cc"
  filete-suave: "#e2e8e2"
  campo-fase-1: "#dcefd2"
  campo-fase-2: "#cfe8e0"
  campo-fase-3: "#d4e5f2"
  campo-fase-4: "#e0e2f0"
typography:
  display:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "clamp(3.4rem, 11vw, 7.5rem)"
    fontWeight: 900
    lineHeight: 0.82
    letterSpacing: "-0.04em"
    fontVariation: "tabular-nums"
  headline:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "clamp(1.35rem, 3.6vw, 2.4rem)"
    fontWeight: 900
    lineHeight: 1.02
    letterSpacing: "-0.02em"
  headline-pagina:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "clamp(1.6rem, 5vw, 3rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "clamp(1rem, 2.4vw, 1.25rem)"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "0.04em"
  ordinal:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontVariation: "tabular-nums"
  ordinal-movil:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontVariation: "tabular-nums"
  body-strong:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "1.08rem"
    fontWeight: 800
    lineHeight: 1.28
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: "normal"
  marca:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "0.94rem"
    fontWeight: 900
    lineHeight: 1.45
    letterSpacing: "0.02em"
  accion:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "0.86rem"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "0.01em"
  subrotulo:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: "0.1em"
  label-lg:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.1em"
  label:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "0.76rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.14em"
  label-sm:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.14em"
  micro:
    fontFamily: "Archivo, 'Segoe UI', system-ui, -apple-system, Arial, sans-serif"
    fontSize: "0.68rem"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "0.08em"
rounded:
  none: "0"
  hairline: "1px"
spacing:
  filete: "4px"
  xs: "6px"
  sm: "8px"
  md: "10px"
  lg: "14px"
  xl: "18px"
  seccion: "26px"
  rotulo: "44px"
  pie: "56px"
  fin: "72px"
  franja: "52px"
  borde-pagina: "clamp(16px, 4vw, 32px)"
  banda: "clamp(18px, 3vw, 30px)"
components:
  franja:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    typography: "{typography.marca}"
    rounded: "{rounded.none}"
    height: "52px"
    padding: "0 clamp(16px, 4vw, 32px)"
  consulta-input:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    rounded: "{rounded.none}"
    padding: "0 56px 0 52px"
    height: "clamp(64px, 9vw, 84px)"
  banda:
    backgroundColor: "{colors.campo-fase-1}"
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    rounded: "{rounded.none}"
    padding: "clamp(18px, 3vw, 30px) clamp(16px, 4vw, 32px)"
  banda-apagada:
    backgroundColor: "#ebf3e7"
    textColor: "#455346"
  fila:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
    padding: "18px 0"
  fila-enlace-hover:
    backgroundColor: "{colors.amarillo}"
    textColor: "{colors.sobre-amarillo}"
  boton-ova:
    backgroundColor: "{colors.verde}"
    textColor: "{colors.sobre-verde}"
    typography: "{typography.accion}"
    rounded: "{rounded.none}"
    padding: "10px 14px"
  boton-ova-hover:
    backgroundColor: "{colors.amarillo}"
    textColor: "{colors.sobre-amarillo}"
  boton-archivo:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    typography: "{typography.accion}"
    rounded: "{rounded.none}"
    padding: "10px 14px"
  boton-archivo-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.papel}"
  marca-compartido:
    backgroundColor: "{colors.filete-suave}"
    textColor: "{colors.ink-medio}"
    rounded: "{rounded.none}"
    padding: "3px 9px"
  rotulo:
    backgroundColor: "{colors.papel}"
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    rounded: "{rounded.none}"
    padding: "0 0 10px"
  rotulo-sub:
    backgroundColor: "{colors.papel}"
    textColor: "{colors.ink-medio}"
    typography: "{typography.subrotulo}"
    rounded: "{rounded.none}"
    padding: "0 0 7px"
---

# Design System: Gestión de redes de datos — SENA 228183

## Overview

**Creative North Star: "The Station Directory, Daylit"**

This is Colombian public-institution wayfinding applied to a course index. The learner arrives
the way a traveller arrives at a terminal: already knowing the destination, needing only to be
told where it is. So the surface behaves like a directory board mounted on a wall — a fixed
identity strip that never leaves, one oversized control, and four full-bleed phase panels that
each own a phase. Nothing here is a "card"; everything is either a field, a rule, or a row.

The whole system is light. Chrome — strip, search bar, count bar, footer — is white panel on a
warm paper wall, ruled with SENA green; the phase panels are pale institutional tints that run
green through teal and blue to violet-grey. Ink is near-black on everything. Density stays high
and the type stays heavy: numerals are set at signage scale, up to 7.5rem, because a directory
that whispers its zone numbers is not a directory.

The defining structural fact of this build is that **the phase colour is not a design token, it
is authored data**. Each phase carries one hex value in `FASES` in `herramientas/generar_sitio.py`,
and the generator derives from it — at build time, with a contrast gate — the ink, the muted ink,
the numeral colour and the dimmed field, then emits them as inline custom properties on that
phase's band and header. The knob is part of the system; so is the gate that keeps it honest.

Confirmed rejections: no dark backgrounds anywhere, no cards as page structure, no eyebrows or
kickers above headings, no cast shadows, no tonal gradients as fill, no photography or
illustration, no icon fonts. The anti-reference is the LMS course catalogue — a hero banner over
a grid of tiles — which is what the previous version of this site was.

**Key Characteristics:**
- Four full-bleed phase panels, one per phase, separated by a 4px paper fillet
- Phase colour authored per phase; every ink on it derived and contrast-gated at build time
- A single search control at signage height; every state on the page derives from it
- One committed look: light only, no dark-scheme fork
- Numerals as the primary display element, always tabular
- Flat by construction: depth is field tint and 1px rules, never shadow
- Zero corner radius except a 1px softening on the focus ring
- Exactly one authored animation in the whole system

## Colors

Pale institutional fields on a paper wall, near-black ink, one green that signs it and one
yellow that means "found".

### Primary
- **Verde SENA** (`{colors.verde}`): the identity mark, used as a ground and a rule — the 4px
  rule under the identity strip, the 4px rule over the footer and under a phase header, the
  scrollbar thumb, the clear button, and the fill of the OVA button. Text on a filled Verde SENA
  control is always **Sobre Verde** (`{colors.sobre-verde}`) — one ink for one ground.
- **Verde Texto** (`{colors.verde-texto}`): the same green made legible on light (5.19:1 on
  paper). It sets the SENA acronym in the strip, the magnifier, the caret, row ordinals, the row
  "go" arrow, the file-type tag, the per-band match counter, and — via derivation — the phase
  numeral on every light field. This is the green that carries text.

### Secondary
- **Amarillo Señal** (`{colors.amarillo}`): reserved, and now strictly a **ground**. It is the
  3px focus outline, the selection highlight, the lit underline of the focused search field, and
  the flood behind a hovered row or button. It is never used as text: on a light surface yellow
  type cannot reach 4.5:1, so the match counters that used to be yellow are Verde Texto.
- **Sobre Amarillo** (`{colors.sobre-amarillo}`) is the primary ink on that ground, **Sobre
  Amarillo Suave** (`{colors.sobre-amarillo-suave}`) the secondary, for the series tag and result
  location inside a hovered row. Yellow never carries white.

### Tertiary — the phase fields (authored)
Four pale fields, one per phase, authored in `FASES` and travelling from institutional green to
blue-violet so the phases read as a sequence:
`{colors.campo-fase-1}` Análisis · `{colors.campo-fase-2}` Planeación ·
`{colors.campo-fase-3}` Ejecución · `{colors.campo-fase-4}` Evaluación.

Each field arrives in the markup as `--campo` on the band and on that phase's header, together
with four values derived from it:

- `--campo-tinta` — near-black `{colors.ink}` on a light field, white on a dark one, picked by
  relative luminance (threshold 0.3). Measured on the shipped fields: 14.24–15.15:1.
- `--campo-suave` — the ink mixed 72% toward the field, for glosa, figures and breadcrumbs.
  Measured: 6.43–6.72:1.
- `--campo-numeral` — `{colors.verde-texto}` on a light field (#5fd424 on a dark one). The field
  identifies the phase; the numeral stays the SENA mark. Measured: 4.02–4.28:1.
- `--campo-apagado` — the field mixed 32% toward paper, for the zero-match state.

`:root` holds fallbacks for all five (`--panel`, `--ink`, `--ink-medio`, `--verde-texto`,
`--papel`) which are used only if a surface never sets a phase.

### Neutral
- **Papel** (`{colors.papel}`) is the wall — body background, the count bar, the gutter behind
  the bands. **Panel** (`{colors.panel}`) is the plate mounted on it: identity strip, search bar,
  every row, every result, the footer.
- **Ink / Ink Medio / Ink Tenue** (`{colors.ink}`, `{colors.ink-medio}`, `{colors.ink-tenue}`):
  the text ramp on paper and panel. Ink Tenue is the floor for small type (5.9:1 on paper); it
  carries the strip's code, the count bar, file weights and the footer.
- **Filete / Filete Suave** (`{colors.filete}`, `{colors.filete-suave}`): the 1px rules under
  rows, the search bar and the count bar, and the flat fill behind status marks.

### Named Rules
**The Authored-Field Rule.** A phase's colour is data, not a token. It lives once, in `FASES`,
and nothing else in the system hard-codes it. A new phase means one hex value — not a new CSS
rule, not a new class, not a fifth `--zona` token.

**The Derived-Ink Rule.** Nothing painted on a phase field is chosen by hand. Ink, muted ink,
numeral and dimmed field are computed from the field, and the generator gates them at build time
— 4.5:1 for text, 3:1 for the numeral — printing a warning that names the offending phase. The
knob cannot silently ship an illegible panel. Any future value that sits on a phase field must be
derived and gated the same way.

**The Dim, Don't Delete Rule.** A phase with zero matches drops to `--campo-apagado` and keeps
its hue, with its numeral, arrow and counter falling to `--campo-suave`. Nothing collapses to a
shared grey, and nothing is removed from the board — the absence is the information the learner
came for.

**The Yellow-Is-A-Ground Rule.** `{colors.amarillo}` is spent only on focus, on the lit search
rule, and on the flood behind a hovered destination — always as a ground, never as text, always
with `{colors.sobre-amarillo}` ink. If you cannot name the state it announces, don't use it.

**The Two Greens Rule.** Verde SENA is the mark and fills grounds; Verde Texto is the green that
carries text on light. They are not interchangeable. A third green (#5fd424) exists only inside
the derivation, as the numeral for a phase field dark enough to need it; it never appears in the
stylesheet.

**The Named-Role Rule.** Every colour in the stylesheet is a custom property with a role in its
name — either a `:root` token or a `--campo-*` value derived from the phase. A hex literal in a
CSS rule means a role nobody has named yet.

**The One Look Rule.** This site commits to a single appearance: `color-scheme: light`, no
`prefers-color-scheme` fork, no theme toggle. The learner on a shared lab machine and the learner
on a phone see the same board. Any future dark treatment is a new decision, not a variant to slip
back in.

## Typography

**Display Font:** Archivo Variable (weights 100–900), self-hosted at
`assets/fonts/archivo-latin.woff2` (latin subset, 35 KB, preloaded, `font-display: swap`)
**Body Font:** the same Archivo, with `Segoe UI, system-ui, -apple-system, Arial, sans-serif`
as the fallback stack.

**Character:** One grotesque doing every job at different weights — the way a signage system uses
one face for the zone numeral, the platform name and the small print. Heavy weights (800–900)
dominate; 500–600 appears only in running glosa and file weights. Uppercase is the default voice
for anything structural.

### Hierarchy
- **Display** (900, `clamp(3.4rem, 11vw, 7.5rem)`, line-height 0.82, -0.04em, tabular): phase
  numerals in the bands and in the phase header. Deliberately above the usual display ceiling —
  signage scale is the thesis, not an accident.
- **Headline** (900, `clamp(1.35rem, 3.6vw, 2.4rem)`, 1.02, -0.02em, uppercase): band names.
- **Headline Página** (900, `clamp(1.6rem, 5vw, 3rem)`, line-height 1, -0.03em, uppercase): the
  phase and documentation `h1`, one step below the band name because the band already named it.
- **Title** (900, `clamp(1rem, 2.4vw, 1.25rem)`, +0.04em, uppercase): section rótulos on a 4px
  ink rule.
- **Ordinal** (900, 1.5rem desktop / 1.2rem below 700px, line-height 1, -0.03em, tabular): the
  row number in the left column.
- **Body Strong** (800, 1.08rem, 1.28, -0.01em): row titles and result titles. This is the
  reading unit of the paper pages — 18.37:1.
- **Body** (500, 1rem, 1.5): glosa prose, capped at `68ch` (`--medida`); also the emphasised
  figure inside a band.
- **Marca** (0.94rem): the identity strip's programme lockup (900/700, uppercase, +0.02em) and
  the band glosa (500, 1.45, capped at 58ch). One size, two weights.
- **Acción** (800, 0.86rem, +0.01em): button and chip labels; uppercase and +0.06em on the OVA
  button.
- **Subrótulo** (800, 0.82rem, +0.1em, uppercase): group sub-headings on a 1px fillet, and the
  truncation note under a long result list.
- **Label LG** (700, 0.8rem, +0.1em to +0.14em, uppercase): band figures, the strip code and the
  footer line.
- **Label** (700, 0.76rem, +0.12em to +0.16em, uppercase): the workhorse — breadcrumbs, section
  counts, the count bar, result locations, file weights.
- **Label SM** (700, 0.72rem, +0.1em to +0.14em, uppercase): the series tag under a row title,
  the status marks, and the clear button.
- **Micro** (900, 0.68rem, +0.08em): the file-type tag inside a download chip.

### The closed ramp

The small-type ramp is closed: 0.72 / 0.76 / 0.80 / 0.82 / 0.86 / 0.94rem, each step carrying two
or more roles, with no single-use value between them. Every size in the build resolves to a role
above. The one authored exception is the row Ordinal, which steps to 1.2rem below 700px because a
44px ordinal column cannot hold a 1.5rem numeral.

Fluid roles are ranges, not steps. A `clamp()` on Display, Headline, Title or the search input
defines endpoints of a continuous curve — the search input's `1.05rem` lower bound is one such
endpoint, not a size in the ramp. Clamp bounds are exempt from the One-Step-Apart Rule; discrete
sizes are not.

Measured contrast on the shipped build: band phase name 14.24–15.15, band glosa and figures
6.43–6.72, band numeral 4.02–4.28; identity lockup 18.37, strip code 5.80, search input 18.37,
count bar 5.28, footer 5.80, row title 18.37. Nothing under 4.5:1 at small sizes.

### Named Rules
**The Numerals-Are-Furniture Rule.** Every number the learner might compare — ordinals, counts,
figures, weights, the programme code — is `font-variant-numeric: tabular-nums`. Digits must line
up column-to-column across rows.

**The No-Eyebrow Rule.** Nothing is set above a heading. A group is announced by a sub-heading
with its own fillet, and qualifiers hang below the title as a series tag. Small uppercase type
above a title is banned outright in this system.

**The Signage-Uppercase Rule.** Uppercase is for structure — names, labels, actions, counts.
Running prose is sentence case. Uppercase a paragraph and the world stops reading as signage and
starts reading as shouting.

**The One-Step-Apart Rule.** Two type sizes that differ by less than a recorded step are the same
size wearing two names. New work picks a role from the hierarchy above; it does not add a size
between two that already exist.

## Layout

A single centred measure of `1180px` (`--ancho`) with `clamp(16px, 4vw, 32px)` side padding —
but the *fields* ignore it. Phase panels, the identity strip, the search bar, the count bar and
the footer are all full-bleed; only their inner container is constrained. That split is the
spatial thesis: colour goes edge to edge, content stays on the measure.

Two stacked sticky layers hold the top of every page: the identity strip at `top: 0`
(`z-index: 30`, 52px tall) and the search bar directly beneath it at `top: var(--franja)`
(`z-index: 29`). They never scroll away, so filtering never costs the learner their position.

The board is a flex column, which lets the filter re-rank bands by match count through
`order: -n` without touching the DOM. Each band is a three-column grid — numeral
(`minmax(96px, 15%)`), body (`1fr`), arrow (`auto`) — with a `clamp(14px, 3vw, 30px)` gap. Rows
below are a two-column grid, `62px` ordinal plus content, becoming three when the row is itself
a link.

Vertical rhythm: rows are `18px` top and bottom against a 1px rule; a section rótulo opens at
`44px`; a sub-group at `26px`; the footer at `56px`; the page ends with `72px`.

One breakpoint governs the layout at `700px`: the band numeral column narrows to
`minmax(58px, 20%)`, row ordinals drop to `44px` and 1.2rem, the result "where" column moves
below its title, and the rótulo count wraps to its own line. A second rule at `420px` removes the
programme name from the identity strip — the acronym and code carry the institutional read at
full size, and a word truncated mid-syllable does not.

**The Field-Bleeds, Content-Measures Rule.** Any coloured surface runs the full viewport width;
its contents sit inside the 1180px container. Never a coloured block inset with margins.

## Elevation & Depth

There are no shadows in this system. Depth is tonal and linear: pale phase fields against the
paper wall, white panels sitting forward on it, and 4px or 1px rules cutting everything else. The
only `box-shadow` declarations in the build are zero-blur inset rings
(`inset 0 0 0 1px var(--filete)`) used as borders on the file chip and the no-OVA mark — they
draw a line, they do not cast light. Sticky layers stack by `z-index` (30 / 29) with a 1px fillet
as their seam.

Because the whole world is light, hover on a field **darkens** rather than lightens:
`filter: brightness(0.955)` on a band. That direction is the rule — pressing a light surface
makes it recede slightly, it never blooms.

**The No-Cast-Shadow Rule.** No `box-shadow` with a blur radius or an offset, anywhere. If a
surface needs separation, give it a different field tint or a fillet.

## Shapes

Zero radius. Every band, row, chip, button, mark and input is a hard rectangle; the only
non-zero corner in the build is a `1px` softening on the focus outline, which exists so the ring
does not needle at the corners. Borders come in exactly two weights: the 4px **filete** (paper
gaps between phase panels, the green rule under the identity strip and over the footer, the green
rule under a phase header, the ink rule under a section rótulo, the lit underline of the focused
search field) and the 1px hairline (row separators, sub-heading rules, the seams under the search
and count bars, inset chip rings).

Iconography is inline SVG only, four glyphs total, all `stroke-width: 2.6`, round caps, drawn in
`currentColor`: a magnifier (22px), a forward arrow (34px), an outbound arrow (15px) and a
download arrow onto a baseline (15px). The stroke weight is chosen to match the type's mass.

**The Two-Weights Rule.** A line in this system is 4px or 1px. There is no 2px and no 3px rule
(the 3px focus outline is a ring, not a rule).

**The Hatch, Not Halftone Rule.** The one patterned fill in the system — the 135° 7px repeating
hatch behind the "sin OVA" mark — is a signage hatch marking an absence. Hatching at a fixed
angle and pitch is native to this world; smooth tonal gradients as decoration are not.

## Components

### Buttons
- **Shape:** hard rectangle (0 radius), `10px 14px` padding, `9px 12px` under 700px.
- **OVA (primary):** Verde SENA field with Sobre Verde ink, uppercase, +0.06em. It is the only
  green-filled control, and it means exactly one thing: open a learning object.
- **Archivo (secondary):** Panel field with a 1px inset ring, carrying three parts inline — the
  micro file-type tag in Verde Texto, the file name, the tabular weight in Ink Tenue, then the
  download glyph.
- **Hover / Focus:** OVA flips to Amarillo with Sobre Amarillo ink. Archivo inverts to an Ink
  field with Papel text, its ring dropped and its type tag flipping to Amarillo. Both transition
  `background` and `color` over 140ms `ease-out`. Focus-visible adds the global 3px Amarillo
  outline at 2px offset.

### Chips / Marks
- **Style:** flat rectangle, `3px 9px`, Label SM at 800 / +0.1em uppercase, inline-flex with a
  7px gap. No radius, no border by default.
- **Shared-OVA mark:** Filete Suave field, Ink Medio text — states that a phase reuses another
  phase's object.
- **No-OVA mark:** the diagonal hatch fill with a 1px inset ring. Absence is drawn as
  deliberately as presence; it is never a blank space.

### Inputs
- **Style:** the search field is the only input. It has no border and no background of its own —
  it sits transparent on the white search bar at `clamp(64px, 9vw, 84px)` tall, padded 52px left
  for the magnifier and 56px right for the clear button, set at `clamp(1.05rem, 2.6vw, 1.5rem)`
  weight 700 in Ink, with a Verde Texto caret and magnifier and an Ink Tenue placeholder.
- **Focus:** the 4px transparent bottom rule under the whole box lights Amarillo over 160ms. The
  native outline is suppressed here and only here — the lit rule *is* the focus indicator. No
  focus box, no glow.
- **Clear:** a Verde SENA pill at the right edge, revealed only when the field has text, going
  Amarillo on hover.

### Navigation
- **Identity strip:** sticky 52px white bar with a 4px Verde SENA bottom rule. `SENA` in Verde
  Texto, the programme name in Ink Medio at 700, both uppercase at Marca size; the code and level
  push right in Ink Tenue at Label LG, tracked and tabular. Under pressure the programme name
  ellipses first and disappears below 420px; the acronym and code never shrink out.
- **Breadcrumbs:** Label size in `--campo-suave` on the phase header, links in `--campo-numeral`
  going to full `--campo-tinta` and underlined on hover — so the breadcrumb is coloured by the
  phase it sits in.
- **Row links:** the whole row is the target. On hover or focus it floods Amarillo, the ordinal
  and the arrow go to Sobre Amarillo, and the series tag drops to Sobre Amarillo Suave.

### Phase Panel (signature)
The system's central device. A full-bleed link, one per phase, painted with that phase's authored
field and separated from the next by a 4px Papel fillet. Inside: the display numeral in
`--campo-numeral`, the uppercase band name in `--campo-tinta`, a `58ch` glosa and a row of real
figures (guides · OVA · downloads) in `--campo-suave`, and the 34px forward arrow at the right.
The same field and the same derived inks paint that phase's page header, which closes with the
4px Verde SENA rule — so arriving on a phase page feels like walking into the panel you pressed.

States: hover and focus darken the whole field with `filter: brightness(0.955)` over 160ms, pull
the numeral and arrow up to `--campo-tinta`, and push the arrow 6px right. Under an active query
each band appends its own match count in Verde Texto and the board re-orders by match count; a
band with zero matches takes `--campo-apagado` and drops its numeral, arrow and counter to
`--campo-suave`.

**Motion.** One authored moment exists in this system: `asentar` — the surviving bands and rows
settle in from `translateY(-7px)` and 0 opacity over 340ms on `cubic-bezier(0.16, 1, 0.3, 1)`,
20ms delay for bands and 30ms for rows, applied to at most the first 12 live elements when a
query re-ranks the board. It is the departures board finishing its flip. Everything else that
moves is a state transition of 140–200ms. `prefers-reduced-motion` collapses every transition
and animation to 1ms.

## Do's and Don'ts

### Do:
- **Do** author a phase's colour once, in `FASES`, and let the generator derive everything painted
  on it.
- **Do** run the build after changing a phase colour and read its contrast warnings; a phase named
  in a warning is not shippable.
- **Do** paint a phase panel full-bleed and separate panels with a 4px `{colors.papel}` fillet.
- **Do** dim an empty phase to `--campo-apagado` with `--campo-suave` ink; never remove it from
  the board.
- **Do** use `{colors.amarillo}` as a ground only — focus, lit search rule, hovered destination —
  always with `{colors.sobre-amarillo}` ink.
- **Do** carry text-weight green with `{colors.verde-texto}` and fill grounds with
  `{colors.verde}`.
- **Do** set every comparable number in tabular figures at signage scale.
- **Do** keep the identity strip and the search bar sticky on every page, in that order (z-index
  30 then 29), so filtering never costs the learner their position.
- **Do** draw absence explicitly — a shared object or a missing OVA gets a mark, not a gap.
- **Do** hold lines to 4px or 1px and corners to 0.
- **Do** state the total: any filtered view says how many of how many matched.

### Don't:
- **Don't** introduce a dark background. This world is light end to end, and there is no
  dark-scheme fork to fall back into.
- **Don't** hard-code a phase colour, or anything derived from one, in the stylesheet.
- **Don't** set `{colors.amarillo}` as text; on a light field it cannot reach 4.5:1.
- **Don't** use cards as page structure. Rows on a panel, panels as fields; no tile grids.
- **Don't** set anything above a heading — no eyebrow, no kicker, no label line.
- **Don't** cast a shadow. Inset zero-blur rings are borders and are the only permitted
  `box-shadow`.
- **Don't** brighten a light surface on hover; press it down (`brightness(0.955)`).
- **Don't** use smooth tonal gradients as fill. (The fixed-pitch diagonal hatch on the "sin OVA"
  mark is a signage hatch and is permitted.)
- **Don't** add photography, illustration, or decorative raster of any kind; this world is type,
  colour fields and inline SVG.
- **Don't** load an icon font or a glyph set. Icons are inline SVG at `stroke-width: 2.6` in
  `currentColor`.
- **Don't** fill a control with green unless it opens an OVA.
- **Don't** introduce a discrete type size between two recorded steps, or a colour literal in a
  rule; every colour is a named role and every size resolves to one.
- **Don't** add a second animation. `asentar` is the system's only authored motion.
- **Don't** restyle anything under `Material de formacion/*/ova/`. Those packages ship
  unmodified; this system governs the index site only.
