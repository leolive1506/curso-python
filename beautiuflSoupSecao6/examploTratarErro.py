from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitulo(url):
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print(f"Ocorreu erro HTTP: {erro}")
        return None
    except URLError as erro:
        print(f"Ocorreu erro URL: {erro}")
        return None
    except:
        print(f"Ocorreu erro na Página: {erro}")
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        titulo = bsObj.body.h1
    except AttributeError as erro:
        print("Ocorreu erro ao tentar acessar a tag h1")
        return None
    except:
        print("Ocorreu erro ao tentar acessar conteudo da página")
        return None
    
    return titulo

titulo = getTitulo(input("Informe a url completa: "))
if titulo is not None:
    print(titulo)
else:
    print("Titulo não encontrado.")