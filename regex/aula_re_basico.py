import re
texto = ("Esta é uma aula de python. Esta aula é sobre expressões regulares. Espere que goste dessa aula.")
# search retorna primeira ocorrencia encontrada
# quando não encontra, retorna none
pattern = "Abrobra"
resultado = re.search(pattern, texto)
# print(resultado)
# retornar o conteudo pesquisado (se não tiver da none e erro ao executar um função em none) -> print(resultado.group())
if resultado:
    print(resultado.group())
else:
    print("Não encontrado")