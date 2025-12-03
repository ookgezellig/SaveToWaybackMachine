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
- [Why frequent commits matter](#why-frequent-commits-matter)
- [Full session log](#full-session-log)

---

## Timeline overview

| Phase | Date | Time | Duration | Commits |
|-------|------|------|----------|---------|
| [Repository reorganization](#phase-1-repository-reorganization-dec-2-session-1) | Dec 2 | 17:02 - 19:52 | 2h 50m | 3 |
| [Screenshot galleries](#phase-2-screenshot-galleries-dec-2-session-1) | Dec 2 | (session 1) | 2h 06m | 5 |
| [GitHub Pages setup](#phase-3-github-pages-setup-dec-2-session-1) | Dec 2 | (session 1) | 40m | 4 |
| [UI refinements](#phase-4-ui-refinements-dec-2-session-1) | Dec 2 | (session 1) | 46m | 6 |
| [Bug fixes & polish](#phase-5-bug-fixes--polish-dec-2-session-1) | Dec 2 | (session 1) | 48m | 5 |
| [KB huisstijl & compliance](#phase-6-kb-huisstijl--compliance-dec-3-session-2) | Dec 3 | (session 2) | ~2h | 6 |
| [Code organization & footer redesign](#phase-7-code-organization--footer-redesign-dec-3-session-2) | Dec 3 | (session 2) | ~1h | 4 |
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

### Phase 2: Screenshot galleries (Dec 2, session 1)

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

### Phase 3: GitHub Pages setup (Dec 2, session 1)

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

### Phase 4: UI refinements (Dec 2, session 1)

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

### Phase 5: Bug fixes & polish (Dec 2, session 1)

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

| Site | Old caption | New caption (from vision) |
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

### Key changes

- Implemented official KB color palette (gold, blue, beige, pink, teal)
- Updated header, footer, links, and navigation with brand colors
- Redesigned footer: black background, white text, white logo
- Added CSS custom properties for easy maintenance
- Ensured WCAG 2.1 AA compliance for all color combinations

📄 **[Full KB huisstijl documentation →](kb-huisstijl.md)**

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

## Why frequent commits matter

One unexpected benefit of working with Claude Code is how it transforms version control from a chore into a natural part of the workflow.

### Before AI assistance

- Writing commit messages was manual and time-consuming
- Developers often batched many changes into single commits
- Git commands required memorization or documentation lookup
- Version control felt like overhead rather than a tool

### With AI assistance

- Commits happen in natural language: "commit and push"
- Each small change gets its own descriptive commit
- Complex Git operations become accessible to all skill levels
- Version control becomes an integral part of the conversation

### Benefits of frequent commits

| Benefit | Description |
|---------|-------------|
| **Detailed history** | Every change is documented with context |
| **Time tracking** | Commit timestamps enable accurate time expenditure analysis |
| **Easy rollback** | Small commits make it simple to undo specific changes |
| **Better collaboration** | Clear history helps others understand the evolution |
| **Learning record** | The commit log becomes a tutorial of the development process |
| **Accountability** | Each decision is recorded with its rationale |

### This project as example

This project has **40+ commits** over two sessions. Each commit represents a logical unit of work:
- Bug fixes get their own commits
- Style changes are separate from structural changes
- Documentation updates are tracked independently

The result is a complete, searchable history that serves as both documentation and a learning resource.

---

## Full session log

The complete session logs with all prompts, actions, and technical details are available at:

📄 **[Session 1 (Dec 2, 2025)](.claude/logs/2025-12-02-session-1.md)** - Repository reorganization, screenshots, GitHub Pages setup

📄 **[Session 2 (Dec 3, 2025)](.claude/logs/2025-12-03-session-1.md)** - KB huisstijl, compliance, code organization, documentation refinements

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
