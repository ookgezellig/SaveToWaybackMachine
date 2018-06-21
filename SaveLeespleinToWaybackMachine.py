#! /usr/bin/env python

import requests, csv, time

# In : Leesplein.nl URL : e.g. https://www.leesplein.nl/jongerenliteratuurplein/auteurs-en-illustratoren/marijn-backer/215
# Out: URL to Wayback Machine (The Internet Archive - TIA) snapshot: e.g. http://web.archive.org/web/20180607161556/https://www.leesplein.nl/jongerenliteratuurplein/auteurs-en-illustratoren/marijn-backer/215
# Works for html pages and pdf + word files in Leesplein.nl

def read_local_csv(filename):
    # Input=local filepath/filename of csv -- Output=List
    list = []
    response = open(filename, 'r')
    sheet = csv.reader(response, delimiter=';')
    for row in sheet:
        if not str(row).startswith('#', 2):  # skip rows in cvs that start with '#'
            list.append(row)
    return list

base_url = 'http://web.archive.org'

urllist = []
urllist=read_local_csv("Input-Leesplein_TeArchiverenURLs_14062018_002.txt") # file with 1 to-be-archived Leesplein-URL per line

with open("Output-Leesplein_GearchiveerdeURLs_14062018_002.txt", "w") as outputfile: # open new versin of outputfile, clear the old version

    for url in urllist:
        #time.sleep(0.3)  # pause for 3 sec, not to overrequest the server
        outputfile = open('Output-Leesplein_GearchiveerdeURLs_14062018_002.txt', 'a') # append to existing outputfile
        linenumber = urllist.index(url)+1
        #print(str(url[0]))
        r = requests.get(base_url + '/save/' + str(url[0])) #This line actually saves to URL to the Waybackmachine. All the following lines of code are for administration/display
        #print(str(r.headers))

        archive_url =""
        if r.headers['X-Cache-Key']: # bestaat niet altijd
            archive_url= r.headers['X-Cache-Key'] # httpweb.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdfNL

            if archive_url.startswith('httpweb.') and archive_url.endswith('NL'):
                archive_url = "http://"+archive_url[4:-2] # http://web.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf
            else: print('Unexpected value of X-Cache-Key in r.headers')

            if r.status_code == requests.codes.ok:
                contenttype = r.headers['Content-Type']
                if "text/html" in contenttype: #html page
                    print(str(linenumber) + "^^^^" + str(url[0])+ "^^^^" + base_url + r.headers['Content-Location']) # the "^^^^" is used a separator between the two URLs. The more traditional separators such as ";" or "," are not reliable enough, as the can occur in URLs.
                    outputfile.write(str(linenumber) + "^^^^" + str(url[0])+ "^^^^" + base_url + r.headers['Content-Location'] + "\n")
                elif contenttype == "application/pdf": #pdf file
                    print(str(linenumber) + "^^^^" + str(url[0]) + "^^^^" + archive_url)
                    outputfile.write(str(linenumber) + "^^^^" + str(url[0]) + "^^^^" + archive_url + "\n")
                elif contenttype == "application/vnd.openxmlformats-officedocument.wordprocessingml.document": #Word doc(x)
                    print(str(linenumber) + "^^^^" + str(url[0]) + "^^^^" + archive_url)
                    outputfile.write(str(linenumber) + "^^^^" + str(url[0]) + "^^^^" + archive_url + "\n")
                else:
                    print("Unknown Content-Type: " + str(contenttype))
            else:
                print('Error in response: ' + str(r.status_code))
        else: print("XXXXXX - No X-Cache-Key returned for this URL")
        outputfile.close()
        
#================= For reference purposes: Files type : html. pdf. docx =================

#Typical r.headers snippet for html-page (better: for 'Content-Type': 'text/html;) --> 'Content-Location' is the relevant part
    # {
    #  'Server': 'nginx/1.13.11',
    #  'Date': 'Fri, 08 Jun 2018 11:16:55 GMT',
    #  'Content-Type': 'text/html;charset=utf-8',
    #  'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive',
    #  'Content-Location': '/web/20180608111639/https://www.leesplein.nl/LL_plein.php?hm=3&sm=3&forward=1&id=197',
    #  'Set-Cookie': 'JSESSIONID=8B20BB411FE218C79AF9636E7EC59E0B; Path=/; HttpOnly',
    #  .....
    #  'X-Cache-Key': 'httpweb.archive.org/save/https://www.leesplein.nl/LL_plein.php?hm=3&sm=3&forward=1&id=197NL',
    # }

# Typical r.headers snippet for pdf file (better: for 'Content-Type': 'application/pdf') --> "X-Cache-Key" is the interesting part
    #     {"Server": "nginx/1.13.11",
    #      "Date": "Fri, 08 Jun 2018 11:04:06 GMT",
    #      "Content-Type": "application/pdf",
    #      .......
    #      "Memento-Datetime": "Fri, 08 Jun 2018 11:04:03 GMT",
    #      "Link": "<https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf>; rel='original', <http://web.archive.org/web/timemap/link/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf>; rel='timemap'; type='application/link-format', <http://web.archive.org/web/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf>; rel='timegate', <http://web.archive.org/web/20180607154335/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf>; rel='first memento'; datetime='Thu, 07 Jun 2018 15:43:35 GMT', <http://web.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf>; rel='memento'; datetime='Fri, 08 Jun 2018 11:04:03 GMT', <http://web.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf>; rel='last memento'; datetime='Fri, 08 Jun 2018 11:04:03 GMT'",
    #       ......
    #      "X-Cache-Key": "httpweb.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdfNL",
    #      "X-Page-Cache": "MISS"
    #      }

# Typical r.headers snippet for docx file (better: for 'Content-Type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document') -->
# --> # 'X-Cache-Key' is the interesting bit
    # {
    # 'Server': 'nginx/1.13.11',
    # 'Date': 'Fri, 08 Jun 2018 11:42:15 GMT',
    # 'Content-Type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    #
    # 'Memento-Datetime': 'Fri, 08 Jun 2018 11:41:53 GMT',
    # 'Link': '<https://www.leesplein.nl/assets/juryrapporten/Leesplein-Doorleestips-15-2016-01.docx>; rel="original", <http://web.archive.org/web/timemap/link/https://www.leesplein.nl/assets/juryrapporten/Leesplein-Doorleestips-15-2016-01.docx>; rel="timemap"; type="application/link-format", <http://web.archive.org/web/https://www.leesplein.nl/assets/juryrapporten/Leesplein-Doorleestips-15-2016-01.docx>; rel="timegate", <http://web.archive.org/web/20180607162805/https://www.leesplein.nl/assets/juryrapporten/Leesplein-Doorleestips-15-2016-01.docx>; rel="first memento"; datetime="Thu, 07 Jun 2018 16:28:05 GMT", <http://web.archive.org/web/20180608114153/https://www.leesplein.nl/assets/juryrapporten/Leesplein-Doorleestips-15-2016-01.docx>; rel="memento"; datetime="Fri, 08 Jun 2018 11:41:53 GMT", <http://web.archive.org/web/20180608114153/https://www.leesplein.nl/assets/juryrapporten/Leesplein-Doorleestips-15-2016-01.docx>; rel="last memento"; datetime="Fri, 08 Jun 2018 11:41:53 GMT"',
    # .....
    # 'X-Cache-Key': 'httpweb.archive.org/web/20180608114153/https://www.leesplein.nl/assets/juryrapporten/Leesplein-Doorleestips-15-2016-01.docxNL',
    # }
