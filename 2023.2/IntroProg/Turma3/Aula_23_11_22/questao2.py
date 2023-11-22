valor_total_conta = float(input("Conta: R$"))

print("Escolha a gorjeta: ")
print("1 - 10%")
print("2 - 15%")
print("3 - 20%")
opcao = int(input("Opção: "))

if opcao == 1:
    gorjeta = 10/100
elif opcao == 2:
    gorjeta = 15/100
elif opcao == 3:
    gorjeta = 20/100

res = valor_total_conta * gorjeta

print(f"Valor da gorjeta: R$ {res}")