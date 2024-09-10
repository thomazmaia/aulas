def menu():
    print("Menu")
    print("0 - Sair")
    print("1 - Add")
    print("2 - del")
    try:
        op = int(input("Digite a opção: "))
        return op
    except ValueError:
         print("Opção inválida. Tente novamente")


while True:
    opcao = menu()
    if opcao == 0:
        print("Saindo...")
        break
    if opcao == 1:
            print("Add...")
            break
    if opcao == 2:
            print("Del...")
            break