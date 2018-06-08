# Saving Leesplein.nl to Wayback Machine

The site www.leesplein.nl will be discontinued in the summer of 2018. (ref https://web.archive.org/web/20180608144204/https://www.bibliotheekblad.nl/nieuws/nieuwsarchief/bericht/1000008395/leesplein_wordt_in_de_zomer_be_c3_abindigd)

To preserve the content of the site (e.g. for sourcing Wikipedia articles) it seemed a good idea to submit a copy in The Wayback Machine of The Internet Archive. (web.archive.org)

We managed to save 1821 URLs of www.leesplein.nl in Wayback Machine (The Internet Archive). 

Steps taken: 

1) We first used https://xmlsitemapgenerator.org/sitemap-generator.aspx to create a raw sitemap for www.leesplein.nl, as a flat list of 2069 URLs. This raw list is available in various formats in the folder 'sitemapLeesplein_07062018'
This list contains html, pdf and docx files

2) We cleaned this raw list, removed non-relevant URLs of non-content pages (e.g. https://www.leesplein.nl/aanvragenboek.php?isbn=9780374302344&amp;title=The Other F-Word&amp;aulast=Friend&amp;aufirst=Natasha) 

3) We then ran 'SaveLeespleinToWaybackMachine.py' to submit the 1821 URLs in this cleaned list to The Wayback Machine.

4) We copy-pasted the Python terminal output to the file 'Output-Leesplein_GearchiveerdeURLs_07062018.csv.txt' (the four '^^^^' in this fil are purely separators). Finally, we derived the Excel-file (.xlsx). 
