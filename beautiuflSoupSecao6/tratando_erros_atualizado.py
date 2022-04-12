from urllib.request import urlopen
from urllib.error import HTTPError
 
html = urlopen("http://localhost:8000/teste.html")
print(f"Html 1: {html}")
 
html = urlopen("http://localhost:8000/naoexiste.html")
print(f"Html 2: {html}")
 
html = urlopen("http://localhost:8000/teste.html")
print(f"Html 3: {html}")


from urllib.request import urlopen
from urllib.error import HTTPError
 
html = urlopen("http://localhost:8000/teste.html")
print(f"Html 1: {html}")
 
try:
    html = urlopen("http://localhost:8000/naoexiste.html")
    print(f"Html 2: {html}")
except HTTPError as erro:
    print(erro)
 
html = urlopen("http://localhost:8000/teste.html")
print(f"Html 3: {html}")


from urllib.request import urlopen
from urllib.error import HTTPError, URLError
 
try:
    html = urlopen("http://localhost:8000/naoexiste.html")
except HTTPError as erro:
    print(f"Erro HTTP: {erro}")
 
try:
    html = urlopen("http://www.xptoxyzabracadabra.com/")
except URLError as erro:
    print(f"Erro URL: {erro}")