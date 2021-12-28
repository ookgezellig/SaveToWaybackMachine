# wbm-archiver script - 30-11-2021 - Improved v2
Script *[SaveToWaybackMachine_v2_30112021.py](SaveToWaybackMachine_v2_30112021.py)* for archiving a list of URLs to the Wayback Machine

This script has three modes: It can
1) save a page/document to the Wayback Machine (WBM) of the Internet Archive (IA)
2) retrieve the latest/newest archived version of a page from the WBM
3) retrieve the oldest/first archived version of a page from the WBM

It uses https://pypi.org/project/waybackpy/, see https://github.com/akamhy/waybackpy/wiki/Python-package-docs for docs and examples.

It was/will be used to archive
* the [old kb.nl](../kb.nl/24122021) website in december 2021
* the [new kb.nl](../kb.nl/xxxx2022) website in Q1 2022

## Notes:
*30/11/2021*
* When archiving/saving pages (mode 1) : script seem to run very stable due to improved error handling
* When archiving/saving pages (mode 1): script runs rather slow  (pm 3 minutes for 10 URLs), this seems to be due to the
  processing speed of the WBM.
* ....
