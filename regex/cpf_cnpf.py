import re
cpf = ("\nOlá cpf 000.000.000-00 e somente numeros 00000000000")
cnpj = ("\nOlá cnpj 00.000.000/0000-00 e somente numeros 00000000000000")

# Somente no começo do texto
pattern = re.compile(r"([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
resultadoCpf = re.findall(pattern, cpf)

print(resultadoCpf)

pattern = re.compile(r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2})")
resultadoCnpj = re.findall(pattern, cnpj)

print(resultadoCnpj)