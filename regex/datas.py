import re
texto = 'Olá hoje é 12/04/2022.'
pattern = re.compile(r"\d{2}/\d{2}/\d{4}")
match = re.findall(pattern, texto)
print(match)