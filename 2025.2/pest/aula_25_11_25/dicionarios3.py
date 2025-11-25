# 1. Como deletar elementos do dicionário
# del
# .pop

inventario = {
    "computador" : 40,
    "datashow" : 1,
    "ar condicionado" : 2,
    "mesa" : 24
}

inventario["computador"] = 39 # Atualizar um item do dicionário

print(inventario["computador"])

del inventario["computador"] # Deletar/apagar um item do dicionário
print("Computador deletado")

inventario.pop("datashow") # Deletar/apagar um item do dicionário
print("Datashow deletado")

print(inventario)

# 2. Como saber o tamanho do dicionário (a quantidade de itens presentes dentro dele)
# len()
print(len(inventario))

# 3. Como verificar se o item existe
# É sempre uma boa prática verificar a existência do item ANTES de deletá-lo
chave = "computador"
if chave in inventario:
    print(f"{chave.upper()} está no inventário")
else:
    print(f"{chave.upper()} não está no inventário")

# 4. Como apagar completamente (limpar) um dicionário
# .clear()
inventario.clear()

print(inventario)
print(len(inventario))

# 5. Como copiar um dicionário 
# .copy()

dicio1 = {
    "one" : 1,
    "two" : 2,
    "three" : 3
}

dicio2 = dicio1.copy()

dicio1["one"] = "um"

print(dicio1)
print(dicio2)

## A cópia é semelhante às listas:
# lista1 = [1, 2, 3]
# lista2 = lista1.copy()

# lista1[0] = "um"

# print(lista1)
# print(lista2)