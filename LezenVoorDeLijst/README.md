# Saving Lezenvoordelijst.nl to Wayback Machine

The site www.lezenvoordelijst.nl will change from 1st August 2018 onwards (see [this message](https://web.archive.org/web/20180718102853/https://www.lezenvoordelijst.nl/blog/2018/lezen-voor-de-lijst-verandert-per-1-augustus/). 

To preserve the current content of the site (e.g. for sourcing Wikipedia articles) it seemed a good idea to submit a copy to The Wayback Machine (web.archive.org).

We managed to save 12.192 URLs of Lezenvoordelijst.nl in the Wayback Machine. 

Steps taken: 

1) We first exported an [input list of 14.096 URLs](Input-LezenVoorDeLijst_TeArchiverenURLs.txt) from Google Analytics. We did some de-duplication and further cleaning, ending up with an input of 14.096 URLs

2) We then ran [SaveLvdLToWaybackMachine.py](SaveLvdLToWaybackMachine.py) to submit these 14.096 URLs to The Wayback Machine. This was not a 100% process, in the end 12.192 URLs were successfully captured (86,5%). 

3) The output of the script was dumped in an 
* [Excel file](Output-LezenVoorDeLijst_GearchiveerdeURLs_18072018.xlsx)
* [Text file](Output-LezenVoorDeLijst_GearchiveerdeURLs_18072018.txt) (using '^^' as a separator)
