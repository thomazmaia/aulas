# Preâmbulo - Dicionários dentro de listas

end1 = {
    "rua" : "rua blabla",
    "numero" : 10,
    "cidade" : "Maranguape"
}

end2 = {
    "rua" : "rua aaaa",
    "numero" : 20,
    "cidade" : "Palmacia"
}

lista_de_end = [end1, end2]

for item in lista_de_end:
    print("--- Endereço: ---")
    for k, v in item.items():
        print(f"{k} - {v}")

