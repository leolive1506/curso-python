import re
texto = 'Olá leonardolivelopes2@gmail.com eu sou o douglas@gmail.com.'
pattern = re.compile(r"[\w.-]+@[\w.-]+")
match = re.findall(pattern, texto)
print(match)