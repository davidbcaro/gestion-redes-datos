---
name: Gestión de redes de datos — SENA 228183
description: Señalética institucional colombiana: bandas de zona a sangre, numerales a escala de señal y un solo control de búsqueda.
colors:
  zona-1: "#103d1b"
  zona-2: "#0a3a38"
  zona-3: "#0b3348"
  zona-4: "#072a45"
  zona-1-off: "#0a1f10"
  zona-2-off: "#081d1c"
  zona-3-off: "#081a24"
  zona-4-off: "#051622"
  tablero: "#0b2e1a"
  tablero-alto: "#103d24"
  tablero-linea: "#1d5334"
  verde: "#39a900"
  verde-vivo: "#5fd424"
  verde-texto: "#2e7d00"
  amarillo: "#fdc300"
  sobre-amarillo: "#22190a"
  sobre-amarillo-suave: "#5c4a08"
  sobre-verde: "#08210b"
  etiqueta-campo-vivo: "#cfe3d5"
  etiqueta-campo: "#8fb39c"
  etiqueta-campo-suave: "#9fc4ae"
  campo-glosa: "#b7cfc0"
  apagado-marca: "#5a7a66"
  apagado-texto: "#7f9689"
  papel: "#f2f5f1"
  panel: "#ffffff"
  ink: "#0a1710"
  ink-medio: "#405146"
  ink-tenue: "#566a5e"
  filete: "#cbd4cc"
  filete-suave: "#e2e8e2"
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
    backgroundColor: "{colors.tablero}"
    textColor: "#ffffff"
    typography: "{typography.marca}"
    rounded: "{rounded.none}"
    height: "52px"
    padding: "0 clamp(16px, 4vw, 32px)"
  consulta-input:
    backgroundColor: "{colors.tablero-alto}"
    textColor: "#ffffff"
    typography: "{typography.headline}"
    rounded: "{rounded.none}"
    padding: "0 56px 0 52px"
    height: "clamp(64px, 9vw, 84px)"
  banda:
    backgroundColor: "{colors.zona-1}"
    textColor: "#ffffff"
    typography: "{typography.headline}"
    rounded: "{rounded.none}"
    padding: "clamp(18px, 3vw, 30px) clamp(16px, 4vw, 32px)"
  banda-apagada:
    backgroundColor: "{colors.zona-1-off}"
    textColor: "{colors.apagado-texto}"
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

**Creative North Star: "The Station Directory"**

This is Colombian public-institution wayfinding applied to a course index. The learner arrives
the way a traveller arrives at a terminal: already knowing the destination, needing only to be
told where it is. So the surface behaves like a departures board bolted to a wall — a fixed
identity strip that never leaves, one oversized control, and four full-bleed zone fields that
each own a phase. Nothing here is a "card"; everything is either a field, a rule, or a row.

The density is high and unapologetic. Type is heavy grotesque, largely uppercase, and numerals
are set at signage scale rather than editorial scale — the phase numeral runs up to 7.5rem
because a directory that whispers its zone numbers is not a directory. Colour is structural,
never ornamental: the four zone fields carry a green-to-institutional-blue ramp so that a phase
is identified by its field, not just by its digit. Paper areas below the board are plain white
panels on a soft warm-grey wall, separated by 1px rules.

Confirmed rejections: no cards as page structure, no eyebrows or kickers above headings, no
cast shadows, no tonal gradients as fill, no photography or illustration, no icon fonts. The
anti-reference is the LMS course catalogue — a hero banner over a grid of tiles — which is what
the previous version of this site was.

**Key Characteristics:**
- Full-bleed horizontal zone bands, one per phase, separated by a 4px paper fillet
- A single search control at signage height; every state on the page derives from it
- Numerals as the primary display element, always tabular
- Flat by construction: depth comes from field darkness and 1px rules, never from shadow
- Zero corner radius everywhere except a 1px softening on the focus ring
- Exactly one authored animation in the whole system

## Colors

A green-to-blue institutional ramp on dark fields, a near-white wall for reading, and one
yellow that means only "active / found".

### Primary
- **Verde SENA** (`{colors.verde}`): the identity mark. It is the strip's bottom border, the
  scrollbar thumb, and the fill of the OVA button — the one action that opens a learning object.
  It is not used for body text anywhere. Text on a filled Verde SENA control is always
  **Sobre Verde** (`{colors.sobre-verde}`) — one ink for one ground.
- **Verde Vivo** (`{colors.verde-vivo}`): the same green pushed bright enough to carry on dark
  fields. It sets the phase numerals, the search magnifier, breadcrumb links, and the band
  arrow. It exists only on `tablero`/`zona` backgrounds.
- **Verde Texto** (`{colors.verde-texto}`): the same green made legible on paper (5.19:1). It
  sets row ordinals and the "go" arrow inside rows, and the file-type tag on download chips. In
  dark scheme it resolves to Verde Vivo.

### Secondary
- **Amarillo Señal** (`{colors.amarillo}`): reserved. It is the focus outline (3px, 2px offset),
  the selection highlight, the search field's lit underline, the match counters, and the hover
  fill of any row or button that is a destination.
- **Sobre Amarillo** (`{colors.sobre-amarillo}`): the primary ink wherever Amarillo is the
  ground — selection, hovered rows, the hovered OVA button. **Sobre Amarillo Suave**
  (`{colors.sobre-amarillo-suave}`) is its secondary, for the series tag and result location
  inside a hovered row. Yellow never carries white.

### Tertiary — the zone ramp
- **Zona 1 · Verde profundo** (`{colors.zona-1}`), **Zona 2 · Verde azulado**
  (`{colors.zona-2}`), **Zona 3 · Azul verdoso** (`{colors.zona-3}`), **Zona 4 · Azul
  institucional** (`{colors.zona-4}`): the four phase fields, full-bleed, all carrying white
  text above 11:1. The ramp travels from SENA green to institutional blue so the phases read as
  a sequence, not four arbitrary colours. `{colors.zona-4}` *is* the institutional blue of this
  system; there is no separate blue token.
- **Off variants** (`{colors.zona-1-off}` … `{colors.zona-4-off}`): the same four fields dimmed
  for the zero-match state. They keep their hue. A phase with no results is still that phase.
- **Apagado Marca** (`{colors.apagado-marca}`) and **Apagado Texto**
  (`{colors.apagado-texto}`): the two inks of a dimmed band — numeral and arrow, then glosa and
  figures. They complete the dim state: field keeps its hue, ink drops two steps.

### Neutral
- **Chapa del tablero** (`{colors.tablero}`): the board plate — identity strip, count bar, and
  the gutter behind the bands. **Tablero Alto** (`{colors.tablero-alto}`) lifts the search bar
  off it; **Tablero Línea** (`{colors.tablero-linea}`) is the 1px seam between them.
- **On-field tints, brightest to faintest:** **Etiqueta Campo Vivo**
  (`{colors.etiqueta-campo-vivo}`) for the programme name in the strip; **Campo Glosa**
  (`{colors.campo-glosa}`) for running prose on a dark field; **Etiqueta Campo**
  (`{colors.etiqueta-campo}`) for every tracked label, figure and code on a dark field;
  **Etiqueta Campo Suave** (`{colors.etiqueta-campo-suave}`) for the search placeholder
  (6.40:1 on Tablero Alto). Four tints, four presences — do not add a fifth.
- **Papel** (`{colors.papel}`) is the wall; **Panel** (`{colors.panel}`) is the plate mounted on
  it — every row and result sits on Panel so the list reads as fixture, not background.
- **Ink / Ink Medio / Ink Tenue** (`{colors.ink}`, `{colors.ink-medio}`, `{colors.ink-tenue}`):
  the paper text ramp. Ink Tenue is the floor for small type (5.9:1 on paper).
- **Filete / Filete Suave** (`{colors.filete}`, `{colors.filete-suave}`): the 1px row rules and
  the flat fill behind status marks.

Dark scheme is a token remap, not a second design: the wall sinks to near-black, Panel rises to
a green-black plate, and Verde Texto resolves to Verde Vivo. The zone ramp does not change,
because the zone ramp is identification.

### Named Rules
**The Zone-Field Rule.** A phase is identified by its field, not by its number. Any new surface
that represents a phase paints the full-bleed zone colour behind it; never a white card with a
coloured accent line.

**The Dim, Don't Delete Rule.** A zone with zero matches drops to its `-off` value and keeps its
hue, while its ink drops to `{colors.apagado-marca}` and `{colors.apagado-texto}`. Nothing
collapses to a shared black, and nothing is removed from the board — the absence is the
information the learner came for.

**The Yellow-Means-Found Rule.** `{colors.amarillo}` is spent only on focus, on match counts, and
on the hover of something that is a destination. It is never a background, a heading colour, a
border, or a decoration. If you cannot name the state it announces, don't use it.

**The Three Greens Rule.** Verde SENA is identity, Verde Vivo is green on dark, Verde Texto is
green on paper. They are not interchangeable and none of them substitutes for another to "match".

**The Named-Role Rule.** Every colour in this build is a custom property with a role in its name.
A hex literal in a rule means a role nobody has named yet — name it or reuse an existing one. The
only literal the system permits is `#fff` on dark fields.

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
  row number in the left column. The one role with an authored mobile step.
- **Body Strong** (800, 1.08rem, 1.28, -0.01em): row titles. This is the reading unit of the
  paper pages — 18.37:1.
- **Body** (500, 1rem, 1.5): glosa prose, capped at `68ch` (`--medida`).
- **Marca** (0.94rem): the two roles that sit at brand size — the identity strip's programme
  lockup (900/700, uppercase, +0.02em) and the band glosa (500, 1.45, capped at 58ch). One size,
  two weights.
- **Acción** (800, 0.86rem, +0.01em): button and chip labels; uppercase and +0.06em on the OVA
  button.
- **Subrótulo** (800, 0.82rem, +0.1em, uppercase): group sub-headings on a 1px fillet, and the
  truncation note under a long result list.
- **Label LG** (700, 0.8rem, +0.1em, uppercase): band figures and the footer line — the label
  step that has to hold up on a dark field.
- **Label** (700, 0.76rem, +0.12em to +0.14em, uppercase): the workhorse — breadcrumbs, section
  counts, result locations, file weights.
- **Label SM** (700, 0.72rem, +0.1em to +0.14em, uppercase): the series tag under a row title and
  the clear button in the search bar.
- **Micro** (900, 0.68rem, +0.08em): the file-type tag inside a download chip.

Measured light-mode contrast on the small tracked type, verified in-browser: file-type tag 5.19,
row ordinal 5.19, file weight 5.80, rótulo count 5.28, sub-heading 7.69, row title 18.37, search
input 12.24.

### The closed ramp

The small-type ramp is closed: 0.72 / 0.76 / 0.80 / 0.82 / 0.86 / 0.94rem, each step carrying two
or more roles, with no single-use value between them. Every size in the build resolves to a role
above. The one authored exception is the row Ordinal, which steps to 1.2rem below 700px because a
44px ordinal column cannot hold a 1.5rem numeral.

Fluid roles are ranges, not steps. A `clamp()` on Display, Headline, Title or the search input
defines endpoints of a continuous curve — the search input's `1.05rem` lower bound is one such
endpoint, not a size in the ramp, and no discrete element is set at it. Clamp bounds are exempt
from the One-Step-Apart Rule; discrete sizes are not.

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
but the *fields* ignore it. Zone bands, the identity strip, the search bar, the count bar and
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

Vertical rhythm on paper: rows are `18px` top and bottom against a 1px rule; a section rótulo
opens at `44px`; a sub-group at `26px`; the footer at `56px`; the page ends with `72px`.

One breakpoint governs the layout at `700px`: the band numeral column narrows to
`minmax(58px, 20%)`, row ordinals drop to `44px` and 1.2rem, the result "where" column moves
below its title, and the rótulo count wraps to its own line. A second, narrower rule at `420px`
removes the programme name from the identity strip entirely — the acronym and code carry the
institutional read, and a word truncated mid-syllable does not.

**The Field-Bleeds, Content-Measures Rule.** Any coloured surface runs the full viewport width;
its contents sit inside the 1180px container. Never a coloured block inset with margins.

## Elevation & Depth

There are no shadows in this system. Depth is entirely tonal and linear: the dark board plate
recedes, the white panel sits forward on the paper wall, and 1px fillets cut everything else.
The only `box-shadow` declarations in the build are zero-blur inset rings
(`inset 0 0 0 1px var(--filete)`) used as borders on the file chip and the no-OVA mark — they
draw a line, they do not cast light. Sticky layers stack by `z-index` (30 / 29) without any
elevation treatment; the seam between them is a 1px `tablero-linea` border.

**The No-Cast-Shadow Rule.** No `box-shadow` with a blur radius or an offset, anywhere. If a
surface needs separation, give it a different field value or a fillet.

## Shapes

Zero radius. Every band, row, chip, button, mark and input is a hard rectangle; the only
non-zero corner in the build is a `1px` softening on the focus outline, which exists so the ring
does not needle at the corners. Borders come in exactly two weights: the 4px **filete** (paper
gaps between zone bands, the green rule under the identity strip, the ink rule under a section
rótulo, the lit underline of the focused search field) and the 1px hairline (row separators,
sub-heading rules, inset chip rings).

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
  `background` and `color` over 140ms `ease-out`. Focus-visible produces the same treatment as
  hover plus the global 3px Amarillo outline.

### Chips / Marks
- **Style:** flat rectangle, `3px 9px`, 800 / +0.1em uppercase, inline-flex with a 7px gap. No
  radius, no border by default.
- **Shared-OVA mark:** Filete Suave field, Ink Medio text — states that a phase reuses another
  phase's object.
- **No-OVA mark:** the diagonal hatch fill with a 1px inset ring. Absence is drawn as
  deliberately as presence; it is never a blank space.

### Inputs
- **Style:** the search field is the only input. It has no border and no background of its own —
  it sits transparent on the Tablero Alto bar at `clamp(64px, 9vw, 84px)` tall, padded 52px left
  for the magnifier and 56px right for the clear button, set at `clamp(1.05rem, 2.6vw, 1.5rem)`
  weight 700 in white, with an Amarillo caret and an Etiqueta Campo Suave placeholder.
- **Focus:** the 4px transparent bottom rule under the whole box lights Amarillo over 160ms. The
  native outline is suppressed here and only here — the lit rule *is* the focus indicator. No
  focus box, no glow.
- **Clear:** a Verde SENA pill at the right edge, revealed only when the field has text, going
  Amarillo on hover.

### Navigation
- **Identity strip:** fixed 52px Tablero bar with a 4px Verde SENA bottom rule. `SENA` in Verde
  Vivo, the programme name in Etiqueta Campo Vivo at 700, both uppercase at Marca size / 900;
  the code and level push right in Etiqueta Campo, tracked and tabular. Under pressure the
  programme name ellipses first and disappears below 420px; the acronym and code never shrink
  out.
- **Breadcrumbs:** Label size in Etiqueta Campo, links in Verde Vivo going Amarillo and
  underlined on hover.
- **Row links:** the whole row is the target. On hover or focus it floods Amarillo, the ordinal
  and the arrow go to Sobre Amarillo, and the series tag drops to Sobre Amarillo Suave.

### Zone Band (signature)
The system's central device. A full-bleed link, one per phase, painted with its zone colour and
separated from the next by a 4px Papel fillet. Inside: the display numeral in Verde Vivo, the
uppercase band name, a `58ch` glosa in Campo Glosa, a row of real figures (guides · OVA ·
downloads) as tracked tabular labels in Etiqueta Campo, and the 34px forward arrow at the right.

States: hover and focus raise the whole field with `filter: brightness(1.45)` over 160ms, turn
the numeral Amarillo and push the arrow 6px right. Under an active query each band appends its
own match count in Amarillo and the board re-orders by match count; a band with zero matches
takes its `-off` field, its numeral and arrow drop to Apagado Marca, and its glosa and figures
to Apagado Texto.

**Motion.** One authored moment exists in this system: `asentar` — the surviving bands and rows
settle in from `translateY(-7px)` and 0 opacity over 340ms on `cubic-bezier(0.16, 1, 0.3, 1)`,
20ms delay for bands and 30ms for rows, applied to at most the first 12 live elements when a
query re-ranks the board. It is the departures board finishing its flip. Everything else that
moves is a state transition of 140–200ms. `prefers-reduced-motion` collapses every transition
and animation to 1ms.

## Do's and Don'ts

### Do:
- **Do** paint a phase with its full-bleed zone field (`{colors.zona-1}` … `{colors.zona-4}`)
  and separate fields with a 4px `{colors.papel}` fillet.
- **Do** dim an empty zone to its `-off` value with Apagado Marca and Apagado Texto ink; never
  remove it from the board.
- **Do** spend `{colors.amarillo}` only on focus, match counts, and destination hover, always
  with `{colors.sobre-amarillo}` ink.
- **Do** pick an on-field tint by presence: Etiqueta Campo Vivo, Campo Glosa, Etiqueta Campo,
  Etiqueta Campo Suave — in that order, and no fifth.
- **Do** set every comparable number in tabular figures at signage scale.
- **Do** keep the identity strip and the search bar sticky on every page, in that order (z-index
  30 then 29), so filtering never costs the learner their position.
- **Do** draw absence explicitly — a shared object or a missing OVA gets a mark, not a gap.
- **Do** hold lines to 4px or 1px and corners to 0.
- **Do** state the total: any filtered view says how many of how many matched.

### Don't:
- **Don't** use cards as page structure. Rows on a panel, bands as fields; no tile grids.
- **Don't** set anything above a heading — no eyebrow, no kicker, no label line.
- **Don't** cast a shadow. Inset zero-blur rings are borders and are the only permitted
  `box-shadow`.
- **Don't** use smooth tonal gradients as fill. (The fixed-pitch diagonal hatch on the "sin OVA"
  mark is a signage hatch and is permitted.)
- **Don't** add photography, illustration, or decorative raster of any kind; this world is type,
  colour fields and inline SVG.
- **Don't** load an icon font or a glyph set. Icons are inline SVG at `stroke-width: 2.6` in
  `currentColor`.
- **Don't** substitute one green for another — `{colors.verde}`, `{colors.verde-vivo}` and
  `{colors.verde-texto}` each have exactly one context.
- **Don't** fill a control with green unless it opens an OVA.
- **Don't** introduce a discrete type size between two recorded steps, or a colour literal in a
  rule; every colour is a named role and every size resolves to one.
- **Don't** add a second animation. `asentar` is the system's only authored motion.
- **Don't** restyle anything under `Material de formacion/*/ova/`. Those packages ship
  unmodified; this system governs the index site only.
