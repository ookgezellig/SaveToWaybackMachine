# Saving KB managed websites to the Wayback Machine

## Using Google sheets to archive pages
without the need to run Python scripts. 
* https://archive.org/services/wayback-gsheets/
* https://twitter.com/LucasWerkmeistr/status/1469742572046368776

Not yet used by KB, but interesting to keep an eye on for future archiving jobs.

## wbm-archiver script - 30-11-2021 - Improved v2 
See the [wbm-archiver_v2_30112021](wbm-archiver_v2_30112021) folder. This Python script was used to [archive kb.nl](kb.nl/24122021) during december 2021.

## wbm-archiver script - 15-7-2021 - OUTDATED, do not use
*Use the [wbm-archiver_v2_30112021](wbm-archiver_v2_30112021) script instead!!* 

<s>On 15-7-2021 I have checked if the [wbm-archiver script from 2 years ago](Literatuurplein/scripts/wbm-archiver/SaveLiteratuurpleinToWaybackMachine.py) was still working. It turned out this was not the case, so I did a small [update of the script](wbm-archiver_15072021/SaveToWaybackMachine.py) to make it work again. However, this script is still not 100% stable or trustworthy and ideally should be checked by a proper developer with knowledge about the WBM and the [Memento protocol](http://mementoweb.org/guide/rfc/) that is used in the WBM. 

It is also noted that the updated script seems to work much slower than 2 years ago, archiving 10 URLs takes approx 2-3 minutes now, while 2 years ago it was approx. 10-20 seconds. This is due to the reduced archiving speed of the WBM itself (this should be verified), not because the updated script itself works slower now. 

So if you plan to archive 10.000s URLs (such as for kb.nl, later in 2021), this will probably take a very long time, and you will probably have to deal with many timeouts, connection failures and errors.</s>

## Archived sites 
* KB website [kb.nl](kb.nl) 
  * The [new kb.nl website](https://www.kb.nl) was launched on 17th March 2022. On the same day, a new, dedicated [KB special collections website](https://collecties.kb.nl) went live as well. Both sites [have been archived](kb.nl/23032022) on 23-24 March 2022.
  * [December 2021](kb.nl/24122021) (old site)
* [Literatuurplein.nl](Literatuurplein) (december 2019)
* [Leesplein.nl](Leesplein) (summer 2018)
* [Lezenvoordelijst.nl](LezenVoorDeLijst) (summer 2018)
<!--* [Literaireprijzen.nl](https://github.com/ookgezellig/SaveToWaybackMachine/tree/master/LiterairePrijzennl)-->
* [Gidsvoornederland.nl](https://www.gidsvoornederland.nl/werken-met-gids/meerwaarde-voor-bibliotheken/bibliotheken-in-nederland) (section with information about public libraries in the Netherlands)

## Aim of this repo
<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Logo_Koninklijke_Bibliotheek_wordmark.svg/150px-Logo_Koninklijke_Bibliotheek_wordmark.svg.png" width="150" align="right"/>

Some websites managed by the [KB, national library of the Netherlands](https://en.wikipedia.org/wiki/Royal_Library_of_the_Netherlands), have been or will be discontinued. To preserve the content of the site (e.g. for sourcing Wikipedia articles) a copy is actively submitted to The Wayback Machine [web.archive.org](https://web.archive.org).
