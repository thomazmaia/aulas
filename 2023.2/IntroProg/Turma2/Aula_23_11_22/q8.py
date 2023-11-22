# 8.  Modifique o programa anterior para solicitar, além do número da tabuada, a operação que o usuário deseja ver a tabuada. Faça um menu do tipo: 0 para tabuada de soma, 1 para tabuada de subtração, etc.

num = int(input("Número: "))
print("1 - Tabuada de SOMA")
print("2 - Tabuada de SUBTRAÇÃO")
print("3 - Tabuada de MULTIPLICAÇÃO")
print("4 - Tabuada de DIVISÃO")
operacao = int(input("Operação: "))

contador = 0

if operacao == 1: # SOMA
    while contador <= 10:
        print(f"{contador} + {num} = {contador+num}")
        contador += 1
elif operacao == 2: # SUBTRAÇÃO
    while contador <= 10:
        print(f"{contador} - {num} = {contador-num}")
        contador += 1
elif operacao == 3: # MULTIPLICAÇÃO
    while contador <= 10:
        print(f"{contador} x {num} = {contador*num}")
        contador += 1    
elif operacao == 4: # DIVISÃO
    while contador <= 10:
            print(f"{contador} / {num} = {contador/num}")
            contador += 1    
else:
    print("Opção inválida.")