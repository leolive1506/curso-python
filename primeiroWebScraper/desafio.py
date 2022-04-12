import re
from urllib.request import urlopen
from urllib.request import Request
req = Request('http://pythonparatodos.com.br/aula.html', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
html = urlopen(req)
textHtml = str(html.read())

patternEmail = re.compile(r"[\w.-]+@[\w.-]+")
math = re.findall(patternEmail, textHtml)
print(math)

patternPhone = re.compile(r'\([0-9]{2}\) [0-9]{5}\-[0-9]{4}')
mathPhone = re.findall(patternPhone, textHtml)
print(mathPhone)