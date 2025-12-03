# Wayback Machine Archiving Project Plan
## Archiving mmdc.nl and manuscripts.kb.nl before Dec 15, 2025 shutdown

**Status:** READY FOR APPROVAL
**Target deadline:** December 15, 2025
**Created:** December 3, 2025
**Days remaining:** ~12 days

---

## User Decisions (Confirmed)

| Decision | Answer |
|----------|--------|
| **Permission** | KB owns these sites - implicit permission to crawl |
| **Priority** | mmdc.nl first (larger, more complex) |
| **URL Source** | Need to crawl (no existing URL list available) |
| **Start** | Immediately after plan approval |
| **Input system** | Simple HTML form with localStorage save functionality |
| **Internal comms** | Email draft + Intranet/Teams post + Social media content |
| **Outreach** | Yes, research medieval manuscripts community contacts |

---

## Executive Summary

This project aims to fully archive two KB-managed medieval manuscript websites to the Internet Archive's Wayback Machine before they go offline on December 15, 2025:

1. **mmdc.nl** - Medieval Manuscripts Digital Collection (database-driven, larger)
2. **manuscripts.kb.nl** - KB Manuscripts portal (static, smaller)

The project includes URL extraction, bulk archiving, verification, documentation, and communications.

---

## Research Findings

### Target Websites Analysis

| Site | Type | robots.txt | Sitemap | Size Estimate |
|------|------|------------|---------|---------------|
| mmdc.nl | Dynamic/Database | Blocks all (`Disallow: /`) | None | Hundreds to thousands |
| manuscripts.kb.nl | Static | Blocks all + 10s delay | None | 10-50 pages + datasets |

**Key Challenge:** Both sites block crawlers via robots.txt and have no sitemaps.

### Existing Infrastructure

**Location:** `D:\KB-OPEN\github-repos\SaveToWaybackMachine\`

**Current scripts:**
- `scripts/wbm-archiver/SaveToWaybackMachine_v2_30112021.py` - Archives URLs to Wayback Machine
- `scripts/capture_*.py` - Playwright-based screenshot capture scripts

**Current workflow:**
1. Input: TXT file with URLs (one per line)
2. Process: waybackpy library submits to Wayback Machine (~3 min per 10 URLs)
3. Output: CSV/XLSX with original + archived URLs
4. Screenshots: Playwright captures with banner trimming

**Limitations to address:**
- No URL crawling/extraction capability
- Slow processing (~18 URLs/hour)
- Manual URL compilation required
- No parallel processing

### Recommended Tools

| Task | Tool | Reason |
|------|------|--------|
| URL Crawling | Crawlee (Python) | Modern async, handles JS, easy setup |
| Wayback Archiving | waybackpy | Already in use, well-maintained |
| JS-heavy pages | Playwright | Already integrated in repo |
| Excel streaming | openpyxl | Native streaming write support |
| Bulk upload | SUCHO email method or IAS3 API | For large batches |

---

## Proposed Project Structure

```
SaveToWaybackMachine/
├── archived-sites/
│   ├── mmdc.nl/                    # NEW
│   │   ├── index.md
│   │   ├── images/
│   │   └── data/
│   │       ├── urls_input.xlsx
│   │       ├── urls_archived.xlsx
│   │       └── crawl_log.json
│   └── manuscripts.kb.nl/          # NEW
│       ├── index.md
│       ├── images/
│       └── data/
├── scripts/
│   ├── wbm-archiver/               # Existing
│   ├── url-crawler/                # NEW
│   │   ├── crawler.py
│   │   ├── sitemap_parser.py
│   │   └── url_extractor.py
│   └── wbm-archiver-v3/            # NEW - Optimized
│       ├── archiver.py
│       ├── batch_processor.py
│       └── verifier.py
├── questionnaire/                   # NEW - User input system
│   ├── index.html
│   ├── questions.json
│   └── responses/
└── communications/                  # NEW
    ├── internal/
    ├── external/
    └── social-media/
```

---

## Phase Breakdown

### Phase 1: Setup & URL Extraction (Days 1-2)

| Step | Task |
|------|------|
| 1.1 | Create folder structure for new sites |
| 1.2 | Develop URL crawler script using Crawlee |
| 1.3 | Crawl mmdc.nl (priority) with throttling |
| 1.4 | Crawl manuscripts.kb.nl with 10s delay |
| 1.5 | Store URLs in Excel with functional groupings |
| 1.6 | Deduplicate and validate URLs |

### Phase 2: Archiver Development (Days 2-3)

| Step | Task |
|------|------|
| 2.1 | Redesign archiver with parallel processing |
| 2.2 | Add progress tracking and resumability |
| 2.3 | Implement better error handling with retry logic |
| 2.4 | Add streaming Excel output |
| 2.5 | Test with small batch (~50 URLs) |
| 2.6 | Validate against existing archived sites |

### Phase 3: Bulk Archiving (Days 3-8)

| Step | Task |
|------|------|
| 3.1 | Submit mmdc.nl URLs to Wayback Machine in batches |
| 3.2 | Submit manuscripts.kb.nl URLs |
| 3.3 | Track progress in Excel (input rows = output rows) |
| 3.4 | Handle failures with retry queue |
| 3.5 | Generate statistics and progress reports |

### Phase 4: Verification & Screenshots (Days 8-10)

| Step | Task |
|------|------|
| 4.1 | Verify all URLs successfully archived |
| 4.2 | Identify and retry failed URLs |
| 4.3 | Capture 6 sample screenshots per site |
| 4.4 | Document any permanent failures |

### Phase 5: Documentation & Site Update (Days 10-11)

| Step | Task |
|------|------|
| 5.1 | Create index.md pages for both sites |
| 5.2 | Add screenshots with captions |
| 5.3 | Update homepage gallery |
| 5.4 | Update archived-sites/index.md |
| 5.5 | Write "how we did it" documentation |

### Phase 6: Communications (Days 11-12)

| Step | Task |
|------|------|
| 6.1 | Draft internal KB email announcement |
| 6.2 | Create Intranet/Teams post |
| 6.3 | Create social media posts (all KB channels) |
| 6.4 | Contact web archiving community |
| 6.5 | Research and contact medieval manuscripts community |

---

## Subagent Strategy (for parallel work)

### Recommended Parallel Agents

| Agent Type | Purpose | When to Use |
|------------|---------|-------------|
| `Explore` | Research websites, find URLs | Phase 1 |
| `Plan` | Design architecture | Setup |
| `code-reviewer` | Review crawler/archiver code | After implementation |
| `general-purpose` | Complex multi-step tasks | URL extraction |

### Suggested Parallel Workflows

**URL Extraction (can run in parallel):**
- Agent 1: Crawl mmdc.nl
- Agent 2: Crawl manuscripts.kb.nl

**Archiving (sequential - rate limits):**
- Single agent with batch processing
- Cannot parallelize due to Wayback Machine rate limits

**Communications (can run in parallel):**
- Agent 1: Draft internal communications
- Agent 2: Research external contacts
- Agent 3: Draft social media posts

---

## Questionnaire System Design

A simple HTML-based questionnaire at `SaveToWaybackMachine/questionnaire/`

**Features:**
- Single-page form with all questions
- LocalStorage for saving intermediate answers
- JSON export of responses
- "Back" and "Edit" functionality
- Final "Submit" button to generate response file

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Sites go offline early | Low | Critical | Start ASAP, prioritize mmdc.nl |
| robots.txt legal issues | Low | High | KB owns sites - implicit permission |
| Wayback Machine rate limiting | High | Medium | Use bulk upload alternatives |
| Incomplete URL discovery | Medium | High | Multiple crawl approaches |
| Time shortage | Medium | High | Prioritize mmdc.nl, defer manuscripts.kb.nl |

---

## Critical Files to Create/Modify

### New Files
| File | Purpose |
|------|---------|
| `archived-sites/mmdc.nl/index.md` | Documentation page |
| `archived-sites/mmdc.nl/data/` | URL lists and archives |
| `archived-sites/manuscripts.kb.nl/index.md` | Documentation page |
| `archived-sites/manuscripts.kb.nl/data/` | URL lists and archives |
| `scripts/url-crawler/crawler.py` | New URL extraction script |
| `scripts/wbm-archiver-v3/archiver.py` | Optimized archiver |
| `questionnaire/index.html` | Simple input form |
| `communications/` | Email drafts and social media content |

### Files to Update
| File | Change |
|------|--------|
| `index.md` | Add new sites to homepage gallery |
| `archived-sites/index.md` | Add new site entries |

---

## Next Steps (After Approval)

1. **Approve this plan** - Review and confirm
2. **Phase 1 begins** - Create folder structure, develop URL crawler
3. **Daily progress updates** - Track in session logs

---

## Technical Details (to be determined during implementation)

| Detail | Proposed Value |
|--------|----------------|
| Excel columns | URL, Section, Archive URL, Archive Date, Status, Notes |
| Screenshot selection | Will identify key pages during crawling |
| Functional groupings | Will discover during site analysis |
| Batch size | 50-100 URLs per batch |
| Retry attempts | 3 retries with exponential backoff |

---

*Plan ready for approval. Implementation will begin immediately upon approval.*

*Last updated: December 3, 2025*
