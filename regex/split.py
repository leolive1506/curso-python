import re
texto = 'ola|hoje|to|lindo'
match = re.split('\|', texto)

texto = 'Ola hoje to lindo'
pattern = re.compile(r"[\w]+ [\w]{1}")
match = re.match(pattern, texto).group()
print(match)
