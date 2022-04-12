import re
texto = ("Esta é uma aula de python")
# com multiline, encontra o Esta apos quebra de linha
# texto = ("Olá, esta é uma aula de python. \nEsta aula é sobre expressões regulares")
# não encontra a palavra esta
# texto = ("Olá, Esta")

pattern = "^Esta"
resultado = re.search(pattern, texto)
resultado = re.search(pattern, texto, re.MULTILINE)

if resultado:
    print(f"*{ resultado.group() }*" )
else:
    print("Não encontrado")