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

# Tratar erros ao acessar dados na web
```py
from urllib.request import urlopen
from urllib.error import HTTPError

# iria da um erro e para tudo pra baixo de não tivesse try
try:
    html = urlopen("http://www.udemy.com/erro")
    print(f"Html 2: {html}")
except HTTPError as erro:
    print(erro)

html = urlopen("http://www.udemy.com/erro")
print(f"Html 3: {html}")
```

- Trantando erro se o servidor nao for encontrado ou der erro na url (URLError)
```py
from urllib.error import URLError
try:
    html = urlopen("http://sdfasdfasdabrobra/erro")
    print(f"Html 2: {html}")
except URLError as erro:
    print(erro)
```

- Ao tentar acessar uma tag de um objeto
    - Verificar se existe
    - Se não existir, retorna none (null)
    - Ao tentar acessar uma tag none terá o erro AttributeError
```py
html = urlopen("http://www.udemy.com")
bsObj = BeautifulSoup(html.read(), 'html.parser)
print(bsObj.html.tag_nao_existente) # retornar none

print(bsObj.html.tag_nao_existente.outra_tag_a_partir_de_outra_que_que_nao_existe) # AttributeError

```

# Temp
Onde está:

teste = bsobj.find_all("", {"class":"comments-link"})

Troque por:

1) Definindo como atributos (attrs):

teste = bsobj.find_all(attrs={"class":"comments-link"})

Ou:   

2) Utilizando "class_":