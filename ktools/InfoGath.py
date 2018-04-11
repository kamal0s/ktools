import urllib.request
import bs4
from bs4 import BeautifulSoup
import urllib.parse
import random
import time

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def Infogathering():
    site = str(input(B+"[+] "+W+"Please Input The Web site That you looking Information about it : "))
    parameter = {"url":site}
    search_parameter = urllib.parse.urlencode(parameter)

    UAS = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       ]
    UA = UAS[random.randrange(len(UAS))]
    header={'User-Agent':UA}
    url = urllib.request.Request('http://toolbar.netcraft.com/site_report?'+search_parameter,headers=header)

    openurl = urllib.request.urlopen(url)
    website = openurl.read()

    soup = BeautifulSoup(website,'html.parser')


    #
    for i in soup.findAll("section",{"id":"history_table"}):
        #for m in soup.findAll("tr",{"class":"TBtr2"}):
            print(P+"[*] "+W+"Trying to Gatharing Information ..... ")

            time.sleep(3)
            print(O+i.tbody.tr.text+W)

    for s in soup.findAll("section",{"id":"background_table"}):

            print(G+s.table.tr.text+W)

    for d in soup.findAll("section",{"id":"network_table"}):
        print(C+d.tbody.text+W)