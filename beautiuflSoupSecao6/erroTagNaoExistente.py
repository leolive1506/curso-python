from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.udemy.com')
bsObj = BeautifulSoup(html.read(), 'html.parser')

try:
    resultado = bsObj.html.tag_nao_existente.vai_da_erro
    print(resultado)
except AttributeError as erro:
    print(f"Erro: {erro}")

# Com if
if bsObj.html.tag_nao_existente is not None:
    print(bsObj.html.tag_nao_existente.outra_tag)
else:
    print("bsObj.html.tag_nao_existente é none")

if bsObj.html is not None:
    resultado = bsObj.html.body
    print('bsObj.html.body ok. bsObj.html não é none')
else:
    print('bsObj.html é none')

if bsObj.html is not None:
    resultado = bsObj.html.bodyTeste
    print(f"resultado: {resultado}") # html não é none então entra no if e o RESULTADO retorna none pois tentou acessar bodyTeste que não existe
else:
    print("bsObj.html é none")