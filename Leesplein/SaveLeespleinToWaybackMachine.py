#! /usr/bin/env python

import requests, csv, time
MAX_RETRIES = 20

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
urllist=read_local_csv("Input-Leesplein_TeArchiverenURLs_14062018_werkbestand.txt") # file with 1 to-be-archived Leesplein-URL per line

with open("Output-Leesplein_GearchiveerdeURLs_14062018_werkbestand.txt", "w") as outputfile: # open new versin of outputfile, clear the old version

    errorfile = open('Output-Leesplein_NogNietGearchiveerdeURLs_14062018_werkbestand.txt', 'a') # deze file bevat alle LP-urls die in de 1e run niet gearchiveerd konden worden

    for url in urllist:
        time.sleep(20)  # pause for 5 sec, not to overrequest the server. Choose longer times for archiving pdf and doc files, as the archiving software needs more time to read these docs than standard html pages
        outputfile = open('Output-Leesplein_GearchiveerdeURLs_14062018_werkbestand.txt', 'a') # append to existing outputfile
        linenumber = urllist.index(url)+1
        #print(str(url[0]))

        #https://stackoverflow.com/questions/33895739/python-requests-cant-load-any-url-remote-end-closed-connection-without-respo
        url_wbm = base_url + '/save/' + str(url[0])
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        session.mount('https://', adapter)
        session.mount('http://', adapter)

        r = session.get(url_wbm)  #This line actually saves to URL to the Waybackmachine. All the following lines of code are for administration/display
        print(str(url[0])+ " -- " + str(r.headers))

# r.headers fout die kan voorkomen: {'Server': 'nginx/1.13.11', ...., 'X-Archive-Wayback-Runtime-Error': 'WaybackException: Unexpected Error', 'Set-Cookie': 'JSESSIONID=9EAAD47DBDCB85D0514293D472995036; Path=/; HttpOnly', 'X-App-Server': 'wwwb-app53', 'X-ts': '----'}

# Als deze fout voorkomt en de LP-URL daardoor niet gearchiveerd wordt: Schrijf niet gearchiveerde LP-url weg naar apart bestand - dat kunnen we dan later als invoer voor een correctierun gebruiken

        if 'X-Archive-Wayback-Runtime-Error' in r.headers:
            errorfile.write(str(url[0]) + "\n")
        else: #r.headers bevat geen Error
            archive_url ="" #only relevant for pdf and doc
            archive_url= r.headers['X-Cache-Key']
            # X-Cache-Key for PDF and DOC: httpweb.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdfNL
            # X-Cache-Key for HTML: httpweb.archive.org/save/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&leefcat=12+&id=6726NL

            if archive_url.startswith('httpweb.') and archive_url.endswith('NL'):
                archive_url = "http://"+archive_url[4:-2]
                # for PDF and DOC : http://web.archive.org/web/20180608110403/https://www.leesplein.nl/assets/juryrapporten/2015-schaduw.pdf
                # for HTML: http://web.archive.org/save/https://www.leesplein.nl/JB_plein.php?hm=3&sm=1&leefcat=12+&id=6726
            else: print('Unexpected value of X-Cache-Key in r.headers')

            if r.status_code == requests.codes.ok:
                contenttype = r.headers['Content-Type']
                if "text/html" in contenttype: #html page -- X-Cache-Key is not relevant
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
        outputfile.close()
        #errorfile.close()

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
