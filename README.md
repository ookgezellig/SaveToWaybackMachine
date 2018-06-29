# Saving Leesplein.nl to Wayback Machine

The site www.leesplein.nl will be discontinued in the summer of 2018. (see [this message](https://web.archive.org/web/20180608144204/https://www.bibliotheekblad.nl/nieuws/nieuwsarchief/bericht/1000008395/leesplein_wordt_in_de_zomer_be_c3_abindigd))

To preserve the content of the site (e.g. for sourcing Wikipedia articles) it seemed a good idea to submit a copy to The Wayback Machine (web.archive.org).

We managed to save 23.844 URLs of Leesplein.nl in the Wayback Machine. 

Steps taken: 

1) We first made an [input list of 25.514 URLs](Input-Leesplein_TeArchiverenURLs.txt). We did this by combining data from  

* https://xmlsitemapgenerator.org/sitemap-generator.aspx: creating a sitemap for www.leesplein.nl, as a flat list of 2069 URLs. This list is available as a zip-file in the folder 'sitemapLeesplein_07062018'. It contains html, pdf and docx files.
* Google Analytics: we made a list of all Leesplein pages that were visited 20+ times over the last 5 years. This gave a list of pm. 24K URLs 

  We combined both lists, did some de-duplication and further cleaning, ending up with an input of 25.514 URLs

3) We then ran [SaveLeespleinToWaybackMachine.py](SaveLeespleinToWaybackMachine.py) to submit these 25.514 URLs to The Wayback Machine. This was not a 100% proces, in the end 23.844 URLs were successfully captured (93,5%). 

4) The output of the script was dumped in an 
* [Excel file](Output-Leesplein_GearchiveerdeURLs_14062018.xlsx)
* [Text file](Output-Leesplein_GearchiveerdeURLs_14062018.txt) (using '^^' as a separator)
