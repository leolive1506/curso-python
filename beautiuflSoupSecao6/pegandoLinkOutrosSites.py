from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://ge.globo.com/')
bsObj = BeautifulSoup(html.read(), 'html.parser')

for link in bsObj.find_all('a'):
    print(link.get('href'))
