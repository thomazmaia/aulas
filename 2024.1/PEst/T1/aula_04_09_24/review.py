dicionario = {
    "pc" : 40,
    "mouse" : 40,
    "ar condicionado" : 2,
    "datashow" : 1
}

# Como acessar elementos
print(dicionario["mouse"])

# Como modificar elementos
dicionario["mouse"] = 39

print(dicionario)

# Como adicionar elementos
dicionario["teclado"] = 40

print(dicionario)

# Como remover elementos
dicionario.pop("mouse")

print(dicionario)