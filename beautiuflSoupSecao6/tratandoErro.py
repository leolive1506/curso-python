from urllib.request import urlopen
from urllib.error import HTTPError, URLError

html = urlopen("http://www.udemy.com")
print(f"Html 1: {html}")

# iria da um erro e para tudo pra baixo de não tivesse try
try:
    html = urlopen("http://www.udemy.com/erro")
    print(f"Html 2: {html}")
except HTTPError as erro:
    print(erro)

html = urlopen("http://www.udemy.com/erro")
print(f"Html 3: {html}")

# - Trantando erro se o servidor nao for encontrado ou der erro na url (URLError)
try:
    html = urlopen("http://sdfasdfasdabrobra/erro")
    print(f"Html 2: {html}")
except URLError as erro:
    print(erro)