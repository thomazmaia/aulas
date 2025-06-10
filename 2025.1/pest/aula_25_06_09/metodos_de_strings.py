string = "ABACAXI melancia UvAaAaAa limão melão"
numero = 1

print(string.capitalize())
print(string.count("a"))
print(string.upper())
print(string.lower())

while True:
    print("Menu")
    print("1 - blablabla")
    print("2 - blablabla")
    print("3 - blablabla")
    opcao = input("Digite a opção: ")
    if opcao.isnumeric():
        if opcao == "1":
            print("Voce digitou a opção 1")
        elif opcao == "2":
            print("Voce digitou a opção 2")
        elif opcao == "3":
            print("Voce digitou a opção 3")
        else:
            print("Opção inválida")
    else:
        print("Opção inválida")