import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.yellowpages.com/search?search_terms=doctors&geo_location_terms=33558")
soup = BeautifulSoup(page.content, "lxml")

for link in soup.find_all("a"):
    #print(link.get("href")) # print Links
    #print(-------------------------------)
    #print(link.text) #Print Link Text
    #print(link.text, link.get("href")) #Print All together
    print("<a href='%s'>%s</a>" %(link.get("href"), link.text))

