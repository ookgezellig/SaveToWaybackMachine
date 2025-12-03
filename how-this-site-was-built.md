---
layout: default
title: How this site was built
---

[← Back to Home](./)

# How this site was built

**An AI-human collaboration journey**

This GitHub Pages site was created in multiple intensive sessions on December 2-3, 2025, through collaboration between a human curator at the KB (National Library of the Netherlands) and Claude Opus 4.5, an AI assistant by Anthropic.

## Table of contents

- [Timeline overview](#timeline-overview)
- [Development phases](#development-phases)
- [Major achievement: AI vision recognition](#major-achievement-ai-vision-recognition)
- [KB huisstijl implementation](#kb-huisstijl-implementation)
- [Accessibility, privacy & licensing](#compliance--accessibility)
- [Full session log](#full-session-log)

---

## Timeline overview

| Phase | Date | Time | Duration | Commits |
|-------|------|------|----------|---------|
| Repository reorganization | Dec 2 | 17:02 - 19:52 | 2h 50m | 3 |
| Screenshot galleries | Dec 3 | 00:28 - 02:34 | 2h 06m | 5 |
| GitHub Pages setup | Dec 3 | 02:34 - 03:14 | 40m | 4 |
| UI refinements | Dec 3 | 03:14 - 04:00 | 46m | 6 |
| Bug fixes & polish | Dec 3 | 04:00 - 04:48 | 48m | 5 |
| KB huisstijl & compliance | Dec 3 | (session 2) | ~2h | 6 |
| Code organization & footer | Dec 3 | (session 2) | ~1h | 4 |
| **Total** | | | **~10 hours** | **33 commits** |

---

## Development phases

### Phase 1: Repository reorganization (Dec 2, session 1)

**Goal:** Transform a flat, disorganized folder structure into a clean, navigable repository.

**Actions:**
- Created hierarchical folder structure (`archived-sites/`, `scripts/`)
- Added `.gitignore` for IDE and system files
- Added CC0 1.0 LICENSE for public domain dedication
- Updated README.md with comprehensive documentation
- Added internal links and accurate URL counts to all site READMEs

**Commits:**
1. `70d72a3` - Reorganize repository structure
2. `a0c030f` - Update READMEs with internal links, image galleries, and accurate URL counts
3. `1cf205e` - Remove .claude and .prompt-page from gitignore and update session log

---

### Phase 2: Screenshot galleries (Dec 2-3, session 1)

**Goal:** Add visual screenshots from the Wayback Machine to showcase each archived site.

**Actions:**
- Created Python scripts using Selenium to capture Wayback Machine pages
- Captured 36 screenshots (6 per site) at deep-level URLs
- Trimmed donation banners (210px from top) for cleaner presentation
- Added responsive image galleries to all README files
- Iterated through multiple screenshot captures to fix errors

**Commits:**
4. `acbaea3` - Add Wayback Machine screenshot galleries to all archived site READMEs
5. `4537732` - Fix Wayback Machine screenshots - remove erroneous captures
6. `533e61b` - Add Wayback Machine screenshots with trimmed donation banners
7. `d77396a` - Replace screenshots with comprehensive deep-level captures
8. `7aebfca` - Update session log with final screenshot improvements

---

### Phase 3: GitHub Pages setup (Dec 2-3, session 1)

**Goal:** Create a browsable website from the repository documentation.

**Actions:**
- Created `_config.yml` with Jekyll configuration
- Built custom `_layouts/default.html` with:
  - Responsive CSS styling
  - Navigation breadcrumbs
  - Card-based navigation
  - Lightbox for image galleries
- Created landing pages for all sections
- Enabled GitHub Pages via API
- Added repository topics for discoverability

**Commits:**
9. `4e39f33` - Add GitHub Pages site with navigation and breadcrumbs
10. `80ff275` - Add screenshot gallery to kb.nl overview page
11. `1f5ffec` - Fix GitHub Pages layout and add index.md files
12. `55e3bfe` - Fix homepage text and sort table by date descending

---

### Phase 4: UI refinements (Dec 2-3, session 1)

**Goal:** Polish the user interface and fix visual issues.

**Actions:**
- Added screenshot thumbnails to homepage navigation cards
- Implemented lightbox with keyboard navigation (← → Esc)
- Fixed table formatting issues
- Extended lightbox to work on all content images
- Reordered tiles by date (descending)

**Commits:**
13. `6e20fbc` - Add screenshots to archived site cards on homepage
14. `ced0b2b` - Fix table formatting, add lightbox for gallery images
15. `1c7cc4e` - Reorder Browse Archived Sites tiles by date (descending)
16. `47f2d4e` - Fix dead links: remove images/ directory links
17. `94eddc9` - Fix pipe character causing table rendering issue
18. `5856154` - Add missing Literatuurplein screenshots

---

### Phase 5: Bug fixes & polish (Dec 2-3, session 1)

**Goal:** Fix remaining issues and improve content quality.

**Actions:**
- Fixed GidsVoorNederland error screenshots
- Added lightbox navigation arrows
- Fixed LezenVoorDeLijst error screenshot
- **Used AI vision to extract meaningful captions from screenshots**
- Changed "Dutch website" to "former Dutch website"
- Added subfolder links
- Reorganized kb.nl galleries by site version

**Commits:**
19. `8f3256a` - Fix GidsVoorNederland screenshots and add lightbox navigation
20. `a599157` - Extend lightbox to all content images
21. `8c4ce2b` - Fix LezenVoorDeLijst error screenshot
22. `7294044` - Fix LezenVoorDeLijst screenshot with blog post page
23. `6f14a67` - Update gallery captions and improve documentation

---

### Phase 6: KB huisstijl & compliance (Dec 3, session 2)

**Goal:** Apply official KB brand colors and add comprehensive compliance documentation.

**Actions:**
- Implemented KB huisstijl color palette as CSS variables
- Updated all design elements (header, links, footer, cards)
- Created full WCAG 2.1 AA accessibility compliance
- Added GDPR/AVG compliance documentation
- Implemented dark mode with KB colors
- Added comprehensive compliance.md page

**Commits:**
24-29. Various commits for KB huisstijl colors, compliance page, accessibility features

---

### Phase 7: Code organization & footer redesign (Dec 3, session 2)

**Goal:** Improve code maintainability and refine footer design.

**Actions:**
- Split inline CSS (~760 lines) into `assets/css/main.css`
- Split inline JavaScript (~200 lines) into `assets/js/lightbox.js`
- Redesigned footer: black background, white text, white KB logo
- Removed gold circles from social media icons

**Commits:**
30. `e49f31f` - Split CSS and JS into separate files
31. `7536c28` - Fix footer styling: all white text, no gold circles, white logo
32-33. Documentation updates

---

## Major achievement: AI vision recognition

### The breakthrough

One of the most significant achievements of this project was using **AI multimodal vision** to automatically extract meaningful captions from screenshot images.

### The problem

Gallery captions were generic and meaningless:
- "Pagina 104937"
- "Boek 277"
- "Boek 287"

### The solution

Claude Opus 4.5 used its native vision capabilities to:
1. **Read each PNG screenshot directly** (not just filenames)
2. **Extract page titles** from Wayback Machine banners
3. **Identify content** - author names, article titles, section headers
4. **Generate meaningful captions** in Dutch and Frisian

### Results

| Site | Old Caption | New Caption (from vision) |
|------|-------------|---------------------------|
| LezenVoorDeLijst | Pagina 104937 | Training verplaatst |
| LezenVoorDeLijst | Pagina 154224 | De man die alles achterliet |
| Leesplein | Boek 277 | Annemarie Bon |
| Leesplein | Boek 287 | Nanda Roep |
| Leesplein | Boek 342 | Ron Langenus |
| Literatuurplein | Prijzen Overzicht | Literaire prijzen |
| Literatuurplein | Canon Overzicht | Canon van de Nederlandse geschiedenis |

### Why this matters

This demonstrates AI can:
- **Replace manual data entry** for image cataloging
- **Extract structured metadata** from screenshot archives
- **Improve accessibility** through automatic alt-text generation
- **Scale to large archives** without human review of each image

---

## KB huisstijl implementation

On December 3, 2025, the site design was updated to align with the official KB (Koninklijke Bibliotheek) house style guidelines. This ensures visual consistency with other KB digital properties.

### Color palette

The site now uses the official KB brand colors defined as CSS custom properties:

| Color | Hex Code | CSS Variable | Usage |
|-------|----------|--------------|-------|
| Gold | #cba052 | `--kb-gold` | Header accent, card hover borders |
| Gold Dark | #8f6a2a | `--kb-gold-dark` | Accent color |
| Blue | #407ec9 | `--kb-blue` | Link hover states, focus indicators |
| Blue Dark | #001a70 | `--kb-blue-dark` | Primary links |
| Pink | #ef6079 | `--kb-pink` | Dark mode visited links |
| Pink Dark | #621323 | `--kb-pink-dark` | Visited links |
| Beige | #ecdcc8 | `--kb-beige` | Breadcrumbs, table headers |
| Teal | #9cdbd9 | `--kb-teal` | Available for accent use |
| Light Blue | #96bded | `--kb-light-blue` | Accent color |

### Design elements updated

| Element | Before | After |
|---------|--------|-------|
| Header border | Gray (#e5e5e5) | KB Gold (#cba052) |
| Link color | Generic blue (#0056b3) | KB Dark Blue (#001a70) |
| Link hover | Darker blue (#003d7a) | KB Blue (#407ec9) |
| Breadcrumbs | Light gray (#f8f9fa) | KB Beige (#ecdcc8) |
| Table headers | Light gray (#f6f8fa) | KB Beige (#ecdcc8) |
| Card hover | Shadow only | Shadow + Gold border |
| Footer background | Gray (#2d3748) | Black (#000) |
| Footer text & headings | Varied | White (#fff) |
| Footer logo | Color KB logo | White KB logo |
| Social icons | With background circles | Transparent (icon only) |

### Implementation approach

1. **CSS Custom Properties** - All KB colors are defined as CSS variables in `:root`, making future updates easy
2. **Consistent hover states** - Gold accents appear on interaction throughout the site
3. **Dark mode support** - KB colors are adapted for dark mode while maintaining brand recognition
4. **WCAG compliance** - All color combinations maintain minimum 4.5:1 contrast ratio

### Source materials

The KB huisstijl implementation was based on:
- Official KB Huisstijlportaal documentation
- Color palette reference images
- CSS variables from KB digital properties

These materials are stored in `.kbhuisstijl-docs/` for reference.

---

## Compliance & accessibility

As a final phase, comprehensive compliance testing and improvements were implemented to ensure the site meets European standards.

### GDPR/AVG compliance

| Aspect | Status |
|--------|--------|
| **Cookies** | None used |
| **Analytics** | No tracking |
| **Personal data** | None collected |
| **Third-party services** | None embedded |

### WCAG 2.1 Level AA

| Feature | Implementation |
|---------|----------------|
| **Skip link** | "Skip to main content" for screen readers |
| **Keyboard navigation** | Full keyboard support throughout |
| **Focus indicators** | 3px blue outline on all focusable elements |
| **Color contrast** | Minimum 4.5:1 ratio (WCAG AA) |
| **ARIA labels** | All interactive elements labeled |
| **Focus trapping** | Modal dialogs trap focus correctly |
| **Reduced motion** | Respects `prefers-reduced-motion` |

### Responsive design

| Breakpoint | Target |
|------------|--------|
| > 768px | Desktop |
| 601-768px | Tablet |
| 401-600px | Mobile |
| ≤ 400px | Small mobile |

Additional features:
- **Landscape orientation** optimization for lightbox
- **Touch swipe** navigation in image galleries
- **Dark mode** support via `prefers-color-scheme`
- **High contrast** mode support via `prefers-contrast`
- **Print styles** for clean printed output

### SEO optimization

| Feature | Implementation |
|---------|----------------|
| **Meta tags** | Title, description, keywords, canonical |
| **Open Graph** | Full social media sharing support |
| **Twitter cards** | Twitter sharing optimization |
| **Schema.org** | JSON-LD structured data (Website, Breadcrumb list, Organization) |

### Security

- **HTTPS enforced** via GitHub Pages
- **`rel="noopener"`** on all external links
- **No external scripts** - all JavaScript inline
- **Static content only** - no server-side processing

📄 **[Full Accessibility, Privacy & Licensing Documentation →](compliance.md)**

---

## Full session log

The complete session log with all prompts, actions, and technical details is available at:

📄 **[.claude/logs/2025-12-02-session-1.md](https://github.com/ookgezellig/SaveToWaybackMachine/blob/main/.claude/logs/2025-12-02-session-1.md)**

---

## Tools used

- **AI assistant:** Claude Opus 4.5 (claude-opus-4-5-20251101) via Claude Code CLI
- **Screenshot capture:** Python + Playwright + Pillow
- **Static site generator:** Jekyll (GitHub Pages)
- **Version control:** Git + GitHub
- **Browser automation:** Playwright (Chromium)

---

## License

The source code and text content of this project are dedicated to the public domain under [CC0 1.0](LICENSE). For image credits and copyright information, see [compliance](compliance#image-credits--copyrights).
