import re
texto = ("\nEsta é uma aula de python. Esta aula é sobre expressões regulares. Espere que goste dessa aula.")

pattern = "."
# pegar uma unica ocorrencia de qualquer caracter, exceto nova linha
resultado = re.search(pattern, texto)
# pegar uma unica ocorrencia de qualquer caracter, incluindo nova linha
resultado = re.search(pattern, texto, re.DOTALL)

if resultado:
    print(f"*{resultado.group()}*" )
else:
    print("Não encontrado")