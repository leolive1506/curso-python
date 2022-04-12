import re
texto = ("\nOlá Esta_ é uma aula de python. Esta aula é sobre expressões regulares. - 04/04/2022")

# Somente no começo do texto
pattern = re.compile("Olá")
resultado = re.match(pattern, texto)
if resultado:
    print(resultado.group())