---
layout: default
title: KB huisstijl implementation
description: How the official KB brand colors and house style were implemented on this site
breadcrumb:
  - title: KB huisstijl implementation
---

[← Back to Home](./)

# KB huisstijl implementation

On December 3, 2025, the site design was updated to align with the official KB (Koninklijke Bibliotheek) house style guidelines. This ensures visual consistency with other KB digital properties.

---

## What is huisstijl?

"Huisstijl" is Dutch for "house style" or "corporate identity". It encompasses the visual elements that make an organization recognizable: colors, typography, logos, and design patterns.

The KB (Koninklijke Bibliotheek - Royal Library of the Netherlands) maintains a comprehensive huisstijl to ensure consistent branding across all its digital and print materials.

---

## Color palette

The site uses the official KB brand colors defined as CSS custom properties:

| Color | Hex code | CSS variable | Usage |
|-------|----------|--------------|-------|
| Gold | #cba052 | `--kb-gold` | Header accent, card hover borders |
| Gold dark | #8f6a2a | `--kb-gold-dark` | Accent color |
| Blue | #407ec9 | `--kb-blue` | Link hover states, focus indicators |
| Blue dark | #001a70 | `--kb-blue-dark` | Primary links |
| Pink | #ef6079 | `--kb-pink` | Dark mode visited links |
| Pink dark | #621323 | `--kb-pink-dark` | Visited links |
| Beige | #ecdcc8 | `--kb-beige` | Breadcrumbs, table headers |
| Teal | #9cdbd9 | `--kb-teal` | Available for accent use |
| Light blue | #96bded | `--kb-light-blue` | Accent color |

### Color swatches

The KB color palette creates a warm, professional appearance with gold as the signature accent color:

- **Primary accent:** Gold (#cba052) - used for highlights and interactive states
- **Text links:** Dark blue (#001a70) - ensures readability and accessibility
- **Backgrounds:** Beige (#ecdcc8) - provides subtle warmth without distraction

---

## Design elements updated

| Element | Before | After |
|---------|--------|-------|
| Header border | Gray (#e5e5e5) | KB gold (#cba052) |
| Link color | Generic blue (#0056b3) | KB dark blue (#001a70) |
| Link hover | Darker blue (#003d7a) | KB blue (#407ec9) |
| Breadcrumbs | Light gray (#f8f9fa) | KB beige (#ecdcc8) |
| Table headers | Light gray (#f6f8fa) | KB beige (#ecdcc8) |
| Card hover | Shadow only | Shadow + gold border |
| Footer background | Gray (#2d3748) | Black (#000) |
| Footer text & headings | Varied | White (#fff) |
| Footer logo | Color KB logo | White KB logo |
| Social icons | With background circles | Transparent (icon only) |

---

## Implementation approach

### 1. CSS custom properties

All KB colors are defined as CSS variables in the `:root` selector:

```css
:root {
  --kb-gold: #cba052;
  --kb-gold-dark: #8f6a2a;
  --kb-blue: #407ec9;
  --kb-blue-dark: #001a70;
  --kb-pink: #ef6079;
  --kb-pink-dark: #621323;
  --kb-beige: #ecdcc8;
  --kb-teal: #9cdbd9;
  --kb-light-blue: #96bded;
}
```

This approach makes future updates easy - change the variable once, and it updates everywhere.

### 2. Consistent hover states

Gold accents appear on interaction throughout the site:
- Cards get a gold border on hover
- Buttons show gold highlights
- Focus states use the KB blue for accessibility

### 3. Dark mode support

KB colors are adapted for dark mode while maintaining brand recognition:
- Background becomes dark gray
- Text becomes light
- Accent colors remain recognizable
- Contrast ratios are maintained

### 4. WCAG compliance

All color combinations maintain minimum 4.5:1 contrast ratio for WCAG 2.1 Level AA compliance:
- Dark blue text on white: 12.6:1 ratio
- White text on black footer: 21:1 ratio
- Gold on white: used only for decorative elements

---

## Footer design

The footer received special attention to match the KB website style:

### Before
- Dark blue background (#001a70)
- Gold headings
- Light blue links
- Social icons with gold circular backgrounds

### After
- Black background (#000)
- White headings
- White links
- Social icons without backgrounds (cleaner look)
- White KB logo (matches dark background)

---

## Source materials

The KB huisstijl implementation was based on:

1. **Official KB huisstijlportaal documentation** - internal brand guidelines
2. **Color palette reference images** - official color specifications
3. **CSS variables from KB digital properties** - extracted from existing KB websites

These materials are stored in `.kbhuisstijl-docs/` for reference.

---

## Why brand consistency matters

Implementing the KB huisstijl serves several purposes:

| Purpose | Benefit |
|---------|---------|
| **Recognition** | Users immediately identify this as a KB project |
| **Trust** | Consistent branding builds credibility |
| **Professionalism** | Attention to detail signals quality |
| **Integration** | The site fits seamlessly with other KB properties |
| **Accessibility** | KB colors are chosen with accessibility in mind |

---

## Technical files

The huisstijl is implemented in:

| File | Purpose |
|------|---------|
| `assets/css/main.css` | All color variables and styling |
| `_layouts/default.html` | Logo references and structure |
| `assets/Logo_koninklijke_bibliotheek.svg` | Color KB logo |
| `assets/Online_wit_Nederlands_KB-logo_0.svg` | White KB logo for footer |

---

## Related pages

- [How this site was built](how-this-site-was-built) - Full development story
- [Accessibility, privacy & licensing](compliance) - WCAG compliance details

---

*Last updated: December 2025*
