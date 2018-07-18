# Saving Lezenvoordelijst.nl to Wayback Machine

The site www.lezenvoordelijst.nl will be discontinued in the summer of 2018. 

To preserve the content of the site (e.g. for sourcing Wikipedia articles) it seemed a good idea to submit a copy to The Wayback Machine (web.archive.org).

We managed to save 12.192 URLs of Lezenvoordelijst.nl in the Wayback Machine. 

Steps taken: 

1) We first exported an [input list of 14.096 URLs](Input-LezenVoorDeLijst_TeArchiverenURLs.txt) from Google Analytics. We did some de-duplication and further cleaning, ending up with an input of 14.096 URLs

2) We then ran [SaveLvdLToWaybackMachine.py](SaveLvdLToWaybackMachine.py) to submit these 14.096 URLs to The Wayback Machine. This was not a 100% process, in the end 12.192 URLs were successfully captured (86,5%). 

3) The output of the script was dumped in an 
* [Excel file](Output-LezenVoorDeLijst_GearchiveerdeURLs_18072018.xlsx)
* [Text file](Output-LezenVoorDeLijst_GearchiveerdeURLs_18072018.txt) (using '^^' as a separator)
