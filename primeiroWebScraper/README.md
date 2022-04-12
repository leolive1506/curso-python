# Oq é executar um web scraper
- realizar solicitações **GET** para um servidor web em busca de uma página específica, ler html da pag e extrair dados para isolar o conteúdo que precisamos
    1. Carregar pags web como strings
    2. Analisar html para localizar as informações que interessam

# Ferramentas
- Requests atraves **urllib** para Carregar as páginas web
- **BeautifulSoup** p realizar a análise de informações

# urllib
- Lib padrão pyhton e contém funções para solicitação de dados web, manipulação de cooies e até alteração de metadados como cabeçalhos e agente do usuário
```py
from urllib.request import urlopen
html = urlopen('http://google.com')
print(html.read())
```

## Funções
- urlopen
    - Usada para abrir objeto remote por meio de uma rede e ler tal objeto
    - Objeto pode ser arquivos HTML, imgs ou qualquer fluxo de arquivos
