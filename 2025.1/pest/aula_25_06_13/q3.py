notas = {}

while True:
    chave = input("Digite a matéria ou 0 para sair: ")
    valor = float(input(f"Digite a nota de {chave}: "))
    if chave != "0":
        notas[chave] = valor
    else:
        break

print(notas)