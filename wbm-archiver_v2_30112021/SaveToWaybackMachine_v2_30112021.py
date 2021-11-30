#! /usr/bin/env python
''''
This improved Wayback Machine Internet Archive archiving script can do two things:
1) It can save a page/document (via an URL) to the Wayback Machine (WBM) of the Internet Archive (IA)
2) It can retrieve the lastest/newest archived version of a page from the WBM

In : URL of webpage/doc e.g. https://www.literatuurplein.nl/detail/wereldkaart/armenie/401
Out: URL to WBM snapshot: e.g. http://web.archive.org/web/DATETIMESTAMP/https://www.literatuurplein.nl/detail/wereldkaart/armenie/401

The URLs to be processed are read from a .txt file, with 1 URL per line

The scripts uses https://pypi.org/project/waybackpy/ + https://github.com/akamhy/waybackpy/wiki/Python-package-docs

Notes:
27/11/2021:
* When archiving/saving pages: script seem to run rather stable due to improved error handling
* When archiving/saving pages: script runs rather slow  (pm 3 minutes for 10 urls), this seems to be due to the
  processing speed of the WBM.
* ...

'''

import csv, time
import waybackpy
from waybackpy.exceptions import WaybackError

def read_local_csv(filename):
    # Input=local filepath/filename of csv -- Output=List
    list = []
    response = open(filename, 'r', encoding="utf8")
    sheet = csv.reader(response, delimiter=';')
    for row in sheet:
        if not str(row).startswith('#', 2):  # skip rows in cvs that start with '#'
            list.append(row)
    return list
    print(list)

user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
inputworkfile="Input-TeArchiverenURLs_werkbestand.txt"
outputworkfile="Output-GearchiveerdeURLs_werkbestand.txt"

urllist = []
urllist=read_local_csv(inputworkfile) # file with 1 URL per line

with open(outputworkfile, "w") as outputfile: # open new version of outputfile, clear the old version

    for url in urllist:
        time.sleep(1)  # pause for 5 sec, not to overrequest the server.
        # Choose longer times for archiving pdf and doc files, as the archiving software needs more time to read these docs than standard html pages
        outputfile = open(outputworkfile, 'a') # append to existing outputfile
        #linenumber = urllist.index(url)+1
        wayback = waybackpy.Url(url[0], user_agent)

 # Code for retrieving lastest version of url/page- uncomment to enable - don't forget the comment/disable the code for saving url/page in WBM/IA below
        try:
            print(str(url[0] + "^^^^" + str(wayback.newest().archive_url)))
            outputfile.write(str(url[0] + "^^^^" + str(wayback.newest().archive_url))+"\n")
        except WaybackError as e:
            print(str(url[0] + "^^^^" + "WaybackError - no newest version available in IA"))
            outputfile.write(str(url[0] + "^^^^" + "WaybackError - no newest version available in IA")+"\n")
        except AttributeError as d:
            print(str(url[0] + "^^^^" + "AttributeError - could not find  newest version in IA"))
            outputfile.write(str(url[0] + "^^^^" + "AttributeError - could not find  newest version in IA")+"\n")

# Code for saving url/page in WBM/IA
#         try:
#             archive = wayback.save()
#             print(str(url[0] + "^^^^" + str(archive.archive_url)))
#             outputfile.write(str(url[0] + "^^^^" + str(archive.archive_url))+"\n")
#         except WaybackError as e:
#             print(str(url[0] + "^^^^" + "WaybackError - could not save page to IA"))
#             outputfile.write(str(url[0] + "^^^^" + "WaybackError - could not save page to IA")+"\n")
#         except AttributeError as d:
#             print(str(url[0] + "^^^^" + "AttributeError - could not save page to IA"))
#             outputfile.write(str(url[0] + "^^^^" + "AttributeError - could not save page to IA")+"\n")

    outputfile.close()

