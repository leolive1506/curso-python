from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://localhost:8000/teste.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')

print(bsObj.h1)
print(bsObj.find_all('a'))
for link in bsObj.find_all('a'):
    print(link)
