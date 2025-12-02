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

| Site | Archive Date | URLs | Notes |
|------|--------------|------|-------|
| [Literatuurplein.nl](archived-sites/Literatuurplein/) | Dec 2019 | 69,618 | Comprehensive literary portal archive |
| [kb.nl](archived-sites/kb.nl/) | Mar 2022 | - | New site + collecties.kb.nl |
| [kb.nl](archived-sites/kb.nl/) | Dec 2021 | - | Old site |
| [Leesplein.nl](archived-sites/Leesplein/) | Summer 2018 | - | Children's reading portal |
| [Lezenvoordelijst.nl](archived-sites/LezenVoorDeLijst/) | Summer 2018 | - | Reading list portal |
| [Literaireprijzen.nl](archived-sites/Literaireprijzen.nl/) | Oct 2018 | - | Literary prizes |
| [Gidsvoornederland.nl](archived-sites/GidsVoorNederland/) | Nov 2018 | - | Library section |
| [Literatuurgeschiedenis.org](archived-sites/Literaruurgeschiedenis.org/) | Mar 2022 | - | Literary history |

## Purpose

Some websites managed by the KB have been or will be discontinued. To preserve their content for Wikipedia sourcing and cultural heritage purposes, the KB actively archives websites to the Wayback Machine at [web.archive.org](https://web.archive.org).

## License

This project is dedicated to the public domain under [CC0 1.0](LICENSE).

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Logo_Koninklijke_Bibliotheek_wordmark.svg/150px-Logo_Koninklijke_Bibliotheek_wordmark.svg.png" width="150"/>
