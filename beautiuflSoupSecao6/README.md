# BeautifulSoup
- Nao vem por padrão no python
```sh
pip install beautifulsoup4
```

# Servidor web
- Sistema que hospeda sites e apps web
    - Python possui um simples que podemos usar p colocar nossos arquivos html que usaremos em nossos testes
1. Definir pasta que que irá conter os arquivos 
    - Entrar na pasta e 
    ```sh
    python -m http.server
    ```

# Utilizar BeautifulSoup
```py
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://localhost:8000/teste.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')

# pega somente um dessa forma
print(bsObj.h1)
# pega somente um dessa forma
print(bsObj.find_all('h1'))
print(bsObj.title)
```

# Pegar somente href
```py
for link in bsObj.find_all('a'):
    print(link.get('href'))
```