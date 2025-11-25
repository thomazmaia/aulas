# 1. Como ITERAR em dicionários
# É possível iterar em dicionários de três formas diferentes:
# - Pelas chaves: keys()
# - Pelos valores: values()
# - Pelo par chave,valor: items()
#
# # Iterando em LISTAS:
# lista = [1, 2, 3, 'uva', True, 3.14]
# for item in lista:
#     print(item)

# # Iterando em STRINGS:
# string = "1234OI tchau"
# for caractere in string:
#     print(caractere)

inventario = {
    "computador" : 40,
    "datashow" : 1,
    "ar condicionado" : 2,
    "mesa" : 24
}

for chave in inventario.keys():
    print(chave)
print(20*"-")

for valor in inventario.values():
    print(valor)
print(20*"-")

for chave, valor in inventario.items():
    print(f"{chave} - {valor}")
print(20*"-")