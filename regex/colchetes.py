import re
texto = ("\nEsta é uma aula de python. Esta aula é sobre expressões regulares. Espere que goste dessa aula - 12/04/2022")

# pegar toas minusculas
pattern = "[a-z]"
# pegar toas maiusculas
pattern = "[A-Z]"

# pegar num de 0-9
pattern = "[0-9]"

# localizar hifen
pattern = "[-0-9]"
resultado = re.findall(pattern, texto)

if resultado:
    print(f"*{resultado}*" )
else:
    print("Não encontrado")