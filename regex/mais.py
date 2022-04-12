import re
texto = ("\nEsta é uma aula de python. Esta aula é sobre expressões regulares.")

# retorna somente os "a"
pattern = "a"

# se não achar retorna um array vazio
pattern = "a+"

resultado = re.findall(pattern, texto)

print(f"*{resultado}*" )
