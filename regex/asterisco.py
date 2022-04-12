import re
texto = ("\nEsta é uma aula de python. Esta aula é sobre expressões regulares.")

# retorna somente os "a"
pattern = "a"
# quando não achar o "a" retorna vazio
pattern = "a*"

resultado = re.findall(pattern, texto)

if resultado:
    print(f"*{resultado}*" )
else:
    print("Não encontrado")