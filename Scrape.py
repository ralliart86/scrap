import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/search?search_terms=doctors&geo_location_terms=33558"
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")
link = soup.find_all("a")

#for link in links:
 #   print("<a href='%s'>%s</a>" %(link.get("href"), link.text)

data = soup.find_all("div", {"class": "info"})

for item in data:
    print(item.contents[0].find_all("a", {"class": "business-name"})[0].text)