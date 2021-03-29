import requests
from bs4 import BeautifulSoup

URL = 'https://requests.readthedocs.io/en/master/index.html?fbclid=IwAR2M7mqocOxzN0echM_qUo-UHXvCzKFQZioOK0-evEJgnpdmo9mvkqL-g0A'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find("div", class_="toctree-wrapper compound")
#print(str(results))
titles = results.find_all("li", class_="toctree-l2")
for t in titles:
	title = t.find("a", class_="reference internal")
	link = t.find("a", class_="reference internal")['href']
	print(title.text," -> ", link, end='\n')

#f = open("content.html", "w")
#f.write(str(soup))