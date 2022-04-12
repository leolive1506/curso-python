import re
texto = ("\nEsta é uma aula de python. Esta aula é sobre expressões regulares. Espere que goste dessa aula")

pattern = "aula$"
resultado = re.search(pattern, texto)

if resultado:
    print(f"*{resultado.group()}*" )
else:
    print("Não encontrado")