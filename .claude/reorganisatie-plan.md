# Reorganisatie Plan - SaveToWaybackMachine

*Aangemaakt: 2025-12-02*
*Laatst bijgewerkt: 2025-12-02*

---

## Voorgestelde Nieuwe Uniforme Folderstructuur

```
SaveToWaybackMachine/
├── .claude/                          # [BEHOUDEN] Claude Code configuratie
├── .idea/                            # [BEHOUDEN] IDE configuratie
├── .prompt-page/                     # [BEHOUDEN] Prompt templates
├── .git/                             # [NIEUW] Git repository
├── .gitignore                        # [NIEUW] Git ignore regels
├── LICENSE                           # [NIEUW] CC0 licentie
├── README.md                         # [BIJWERKEN] Project documentatie
│
├── scripts/                          # Alle Python scripts
│   └── wbm-archiver/
│       ├── SaveToWaybackMachine_v2_30112021.py
│       ├── SaveToWaybackMachine_v2_30112021_improvedVeraDeKok.py
│       └── README.md                 # Script documentatie
│
└── archived-sites/                   # [NIET WIJZIGEN] Gearchiveerde website data
    ├── GidsVoorNederland/
    │   └── README.md                 # ✅ AANGEMAAKT
    ├── Leesplein/
    │   └── README.md                 # ✅ AANGEMAAKT
    ├── LezenVoorDeLijst/
    │   └── README.md                 # ✅ AANGEMAAKT
    ├── Literaireprijzen.nl/
    │   └── README.md                 # ✅ AANGEMAAKT
    ├── Literatuurplein/
    │   └── README.md                 # (bestond al)
    ├── Literaruurgeschiedenis.org/
    │   └── README.md                 # ✅ AANGEMAAKT
    └── kb.nl/
        └── README.md                 # ✅ AANGEMAAKT
```

---

## Stap-voor-Stap Instructies

### Fase 1: Backup (VOLTOOID ✅)

- ✅ Backup aangemaakt: `D:\KB-OPEN\github-repos\SaveToWaybackMachine_BACKUP_20251202` (76 MB)

### Fase 2: README bestanden voor archived-sites (VOLTOOID ✅)

**Hoofdfolders:**
- ✅ GidsVoorNederland/README.md aangemaakt
- ✅ kb.nl/README.md aangemaakt
- ✅ Leesplein/README.md aangemaakt
- ✅ LezenVoorDeLijst/README.md aangemaakt
- ✅ Literaireprijzen.nl/README.md aangemaakt
- ✅ Literaruurgeschiedenis.org/README.md aangemaakt
- (Literatuurplein/README.md bestond al)

**kb.nl subfolders:**
- ✅ kb.nl/24122021/README.md aangemaakt (oude site, dec 2021)
- ✅ kb.nl/23032022/README.md aangemaakt (nieuwe site, mrt 2022)
- ✅ kb.nl/sources/README.md aangemaakt (brondata Wikimedia)

### Fase 3: Opschonen Lokale Folder

**Stap 3.1** - Verwijder Windows artifact
```bash
del "D:\KB-OPEN\github-repos\SaveToWaybackMachine\nul"
```

### Fase 4: Nieuwe Bestanden Toevoegen

**Stap 4.1** - Maak `.gitignore` aan

```gitignore
# IDE
.idea/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/

# OS
.DS_Store
Thumbs.db
desktop.ini
nul

# Logs
*.log

# Tijdelijke bestanden
*.tmp
*.temp
~$*
```

**Stap 4.2** - Maak `LICENSE` aan (CC0)

```
CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

The person who associated a work with this deed has dedicated the work to the
public domain by waiving all of his or her rights to the work worldwide under
copyright law, including all related and neighboring rights, to the extent
allowed by law.

You can copy, modify, distribute and perform the work, even for commercial
purposes, all without asking permission.

https://creativecommons.org/publicdomain/zero/1.0/
```

### Fase 5: Git Initialisatie en Synchronisatie

**Stap 5.1** - Initialiseer Git in lokale folder
```bash
cd "D:\KB-OPEN\github-repos\SaveToWaybackMachine"
git init
```

**Stap 5.2** - Voeg GitHub remote toe
```bash
git remote add origin https://github.com/ookgezellig/SaveToWaybackMachine.git
```

**Stap 5.3** - Fetch bestaande GitHub geschiedenis
```bash
git fetch origin
```

**Stap 5.4** - Lokale structuur als nieuwe basis (AANBEVOLEN)
```bash
git checkout -b main
git add .
git commit -m "Reorganize repository structure

- Move archived sites to archived-sites/ folder
- Consolidate scripts in scripts/wbm-archiver/
- Add README.md to each archived site folder
- Add .gitignore and CC0 LICENSE
- Update main README.md"
git push -u origin main --force
```

### Fase 6: README.md Bijwerken

Nieuwe README.md inhoud - zie hieronder.

---

## Nieuwe README.md

```markdown
# SaveToWaybackMachine

Scripts and data for archiving KB-managed websites to the Internet Archive's Wayback Machine.

*Maintained by [KB, national library of the Netherlands](https://www.kb.nl)*

## Repository Structure

```
SaveToWaybackMachine/
├── scripts/                    # Python archiving scripts
│   └── wbm-archiver/          # Wayback Machine archiver
└── archived-sites/            # Archived website data by site
    ├── GidsVoorNederland/
    ├── Leesplein/
    ├── LezenVoorDeLijst/
    ├── Literaireprijzen.nl/
    ├── Literatuurplein/
    ├── Literaruurgeschiedenis.org/
    └── kb.nl/
```

Each archived site folder contains a README.md with details about the archived content.

## Scripts

### wbm-archiver (v2 - 30-11-2021)

Location: `scripts/wbm-archiver/`

This Python script has three modes:
1. Save pages to the Wayback Machine
2. Retrieve the latest archived version of a page
3. Retrieve the oldest archived version of a page

**Requirements:** Python 3.x, waybackpy

**Usage:** See the README in the scripts folder.

## Alternative: Google Sheets Method

Archive pages without running Python scripts:
- https://archive.org/services/wayback-gsheets/

## Archived Sites

| Site | Archive Date | Notes |
|------|--------------|-------|
| kb.nl | Mar 2022 | New site + collecties.kb.nl |
| kb.nl | Dec 2021 | Old site |
| Literatuurplein.nl | Dec 2019 | |
| Leesplein.nl | Summer 2018 | |
| Lezenvoordelijst.nl | Summer 2018 | |
| Literaireprijzen.nl | Oct 2018 | |
| Gidsvoornederland.nl | Nov 2018 | Library section |
| Literatuurgeschiedenis.org | Mar 2022 | |

## Purpose

Some websites managed by the KB have been or will be discontinued. To preserve
their content for Wikipedia sourcing and cultural heritage purposes, the KB
actively archives websites to the Wayback Machine at [web.archive.org](https://web.archive.org).

## License

This project is dedicated to the public domain under [CC0 1.0](LICENSE).

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Logo_Koninklijke_Bibliotheek_wordmark.svg/150px-Logo_Koninklijke_Bibliotheek_wordmark.svg.png" width="150"/>
```

---

## Volgorde van Operaties

1. ✅ Backup maken van lokale folder
2. ✅ README.md bestanden aanmaken voor archived-sites subfolders
3. ✅ Externe links analyse (Wikimedia sites)
4. ✅ Literatuurplein README.md bijgewerkt (gebroken script-links gefixed)
5. 🔲 Opschonen - verwijder `nul` bestand
6. 🔲 Toevoegen - `.gitignore` en `LICENSE`
7. 🔲 Git init - initialiseer repository
8. 🔲 Remote toevoegen - link naar GitHub
9. 🔲 Fetch - haal bestaande geschiedenis op
10. 🔲 README.md bijwerken (root)
11. 🔲 Commit - alle wijzigingen committen
12. 🔲 Push - synchroniseer met GitHub
13. 🔲 **Wikidata pagina bijwerken** (na push!)

---

## Externe Links die Bijgewerkt Moeten Worden

### Wikidata:WikiProject Dutch Literary Awards

**Pagina:** https://www.wikidata.org/wiki/Wikidata:WikiProject_Dutch_Literary_Awards

**Huidige links (verwijzen naar `master` branch en root):**
```
https://github.com/ookgezellig/SaveToWaybackMachine/tree/master/Literatuurplein
https://github.com/ookgezellig/SaveToWaybackMachine/blob/master/Literatuurplein/literatuurplein-prijzen-edities_06122019.tsv
https://github.com/ookgezellig/SaveToWaybackMachine/blob/master/Literatuurplein/literatuurplein-prijzen-edities_06122019.xlsx
https://github.com/ookgezellig/SaveToWaybackMachine/blob/master/Literatuurplein/literatuurplein-prijzen-totaal_17122019.tsv
https://github.com/ookgezellig/SaveToWaybackMachine/blob/master/Literatuurplein/literatuurplein-prijzen-totaal_17122019.xlsx
https://github.com/ookgezellig/SaveToWaybackMachine/blob/master/Literatuurplein/literatuurplein-prijzen_06122019.tsv
https://github.com/ookgezellig/SaveToWaybackMachine/blob/master/Literatuurplein/literatuurplein-prijzen_06122019.xlsx
```

**Nieuwe links (na reorganisatie):**
```
https://github.com/ookgezellig/SaveToWaybackMachine/tree/main/archived-sites/Literatuurplein
https://github.com/ookgezellig/SaveToWaybackMachine/blob/main/archived-sites/Literatuurplein/literatuurplein-prijzen-edities_06122019.tsv
https://github.com/ookgezellig/SaveToWaybackMachine/blob/main/archived-sites/Literatuurplein/literatuurplein-prijzen-edities_06122019.xlsx
https://github.com/ookgezellig/SaveToWaybackMachine/blob/main/archived-sites/Literatuurplein/literatuurplein-prijzen-totaal_17122019.tsv
https://github.com/ookgezellig/SaveToWaybackMachine/blob/main/archived-sites/Literatuurplein/literatuurplein-prijzen-totaal_17122019.xlsx
https://github.com/ookgezellig/SaveToWaybackMachine/blob/main/archived-sites/Literatuurplein/literatuurplein-prijzen_06122019.tsv
https://github.com/ookgezellig/SaveToWaybackMachine/blob/main/archived-sites/Literatuurplein/literatuurplein-prijzen_06122019.xlsx
```

**Actie:** Na de GitHub push moet deze Wikidata pagina handmatig of via de MediaWiki API worden bijgewerkt.
