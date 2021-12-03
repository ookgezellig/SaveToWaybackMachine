# wbm-archiver script - 30-11-2021 - Improved v2
Strongly improved script [SaveToWaybackMachine_v2_30112021.py](wbm-archiver_v2_30112021/SaveToWaybackMachine_v2_30112021.py) using https://pypi.org/project/waybackpy/ 

This improved Wayback Machine Internet Archive archiving script has three modes:
1) It can save a page/document to the Wayback Machine (WBM) of the Internet Archive (IA)
2) It can retrieve the latest/newest archived version of a page from the WBM
3) It can retrieve the oldest/first archived version of a page from the WBM

The script uses https://pypi.org/project/waybackpy/ + https://github.com/akamhy/waybackpy/wiki/Python-package-docs

## Notes:
*30/11/2021*
* When archiving/saving pages (mode 1) : script seem to run rather stable due to improved error handling
* When archiving/saving pages (mode 1): script runs rather slow  (pm 3 minutes for 10 urls), this seems to be due to the
  processing speed of the WBM.
* ....
