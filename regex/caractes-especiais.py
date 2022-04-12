import re
texto = ("\nEsta_ é uma aula de python. Esta aula é sobre expressões regulares. - 04/04/2022")

# somente numeros
pattern = "\d"

# todos que não são digitos (numeros)
pattern = "\D"

# qualquer espaçamento
pattern = "\s"

# qualquer que não seja espaçamento
pattern = "\S"

# qualquer alfanúmerico ou sublinhado
pattern = "\w"

# qualquer que n seja alfanúmerico ou sublinhado
pattern = "\W"

# pegar somente numeros com "N" ocorrências da expressão
# ex: \d{2} somente numeros com dois digitos
pattern = "\d{2}"

# isso ou aquilo  
pattern = "(a) | (\d)"

resultado = re.findall(pattern, texto)

print(f"*{resultado}*" )