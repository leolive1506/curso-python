import re
texto = ("\nEsta_ é uma aula de python. Esta aula é sobre expressões regulares. - 04/04/2022")

# todos "e" minusculo
pattern =re.compile("e")

# ignorando os cases
pattern =re.compile("e", re.IGNORECASE)

resultado = re.findall(pattern, texto)

print(f"*{resultado}*" )