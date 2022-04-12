import re
texto = 'Olá leonardolivelopes2@gmail.com eu sou o douglas@gmail.com.'
pattern = re.compile(r'([\w.-]+)@([\w.-]+)')
resultado = re.search(pattern, texto)

print("resultado.group()", resultado.group())
print("resultado.group(1)", resultado.group(1))
print("resultado.group(2)", resultado.group(2))

resultado = re.findall(pattern, texto)
for email in resultado:
    print(email)