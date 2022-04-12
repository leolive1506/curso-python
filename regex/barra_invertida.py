import re
texto = ("\nEsta é uma aula de python. Esta aula é sobre expressões regulares. Espere que goste dessa aula.")

# assim pegar qualquer primeiro caracter
# pattern = "."
# assim permite filtrar pelo ponto
pattern = "\."
resultado = re.search(pattern, texto)

if resultado:
    print(f"*{resultado.group()}*" )
else:
    print("Não encontrado")