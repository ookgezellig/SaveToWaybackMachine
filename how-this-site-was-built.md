---
layout: default
title: How This Site Was Built
---

[← Back to Home](./)

# How This Site Was Built

**An AI-Human Collaboration Journey**

This GitHub Pages site was created in a single intensive session on December 2-3, 2025, through collaboration between a human curator at the KB (National Library of the Netherlands) and Claude Opus 4.5, an AI assistant by Anthropic.

## Table of Contents

- [Timeline Overview](#timeline-overview)
- [Development Phases](#development-phases)
- [Time Investment](#time-investment)
- [Major Achievement: AI Vision Recognition](#major-achievement-ai-vision-recognition)
- [Compliance & Accessibility](#compliance--accessibility)
- [Full Session Log](#full-session-log)

---

## Timeline Overview

| Phase | Time | Duration | Commits |
|-------|------|----------|---------|
| Repository Reorganization | 17:02 - 19:52 | 2h 50m | 3 |
| Screenshot Galleries | 00:28 - 02:34 | 2h 06m | 5 |
| GitHub Pages Setup | 02:34 - 03:14 | 40m | 4 |
| UI Refinements | 03:14 - 04:00 | 46m | 6 |
| Bug Fixes & Polish | 04:00 - 04:48 | 48m | 5 |
| **Total** | | **~7 hours** | **23 commits** |

---

## Development Phases

### Phase 1: Repository Reorganization (17:02 - 19:52)

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

### Phase 2: Screenshot Galleries (00:28 - 02:34)

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

### Phase 3: GitHub Pages Setup (02:34 - 03:14)

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

### Phase 4: UI Refinements (03:14 - 04:00)

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

### Phase 5: Bug Fixes & Polish (04:00 - 04:48)

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

## Time Investment

Based on git commit timestamps:

| Date | Start | End | Duration |
|------|-------|-----|----------|
| 2025-12-02 | 17:02 | 19:52 | 2h 50m |
| 2025-12-03 | 00:28 | 04:48 | 4h 20m |
| **Total** | | | **~7 hours 10 minutes** |

**Commits:** 23 total
**Files changed:** 100+
**Lines of code:** ~3,000

---

## Major Achievement: AI Vision Recognition

### 🎯 The Breakthrough

One of the most significant achievements of this project was using **AI multimodal vision** to automatically extract meaningful captions from screenshot images.

### The Problem

Gallery captions were generic and meaningless:
- "Pagina 104937"
- "Boek 277"
- "Boek 287"

### The Solution

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

### Why This Matters

This demonstrates AI can:
- **Replace manual data entry** for image cataloging
- **Extract structured metadata** from screenshot archives
- **Improve accessibility** through automatic alt-text generation
- **Scale to large archives** without human review of each image

---

## Compliance & Accessibility

As a final phase, comprehensive compliance testing and improvements were implemented to ensure the site meets European standards.

### GDPR/AVG Compliance

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

### Responsive Design

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

### SEO Optimization

| Feature | Implementation |
|---------|----------------|
| **Meta tags** | Title, description, keywords, canonical |
| **Open Graph** | Full social media sharing support |
| **Twitter Cards** | Twitter sharing optimization |
| **Schema.org** | JSON-LD structured data (WebSite, BreadcrumbList, Organization) |

### Security

- **HTTPS enforced** via GitHub Pages
- **`rel="noopener"`** on all external links
- **No external scripts** - all JavaScript inline
- **Static content only** - no server-side processing

📄 **[Full Compliance Documentation →](compliance.md)**

---

## Full Session Log

The complete session log with all prompts, actions, and technical details is available at:

📄 **[.claude/logs/2025-12-02-session-1.md](https://github.com/ookgezellig/SaveToWaybackMachine/blob/main/.claude/logs/2025-12-02-session-1.md)**

---

## Tools Used

- **AI Assistant:** Claude Opus 4.5 (claude-opus-4-5-20251101) via Claude Code CLI
- **Screenshot Capture:** Python + Selenium + Pillow
- **Static Site Generator:** Jekyll (GitHub Pages)
- **Version Control:** Git + GitHub
- **Browser Testing:** Chrome (headless)

---

## License

This documentation and the entire project are dedicated to the public domain under [CC0 1.0](LICENSE).
