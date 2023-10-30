# Crie um programa que simule um caixa eletrônico. Solicite ao usuário que insira
# o valor que deseja sacar e, em seguida, verifique se o valor é menor ou igual ao
# saldo da conta. Se for, pergunte se o usuário deseja realizar uma retirada
# adicional e, se sim, verifique se o valor adicional também está disponível na
# conta.

saldo = 100
print(f"Saldo na conta: R${saldo}")
saque = float(input("Saque: R$"))

if saque <= saldo:
    saldo = saldo - saque
    pergunta_adicional = input("Você deseja fazer um saque adicional? <sim/nao> ")
    if pergunta_adicional == "sim":
        valor_adicional = float(input("Saque: R$"))
        if valor_adicional <= saldo:
            saldo = saldo - valor_adicional
        else:
            print("Saldo indisponível")
else:
    print("Saldo indisponível")

print(f"Saldo final: R${saldo}")
