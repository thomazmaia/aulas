def verifica_maior(num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    return maior


A = int(input("Digite o 1o numero: "))
B = int(input("Digite o 2o numero: "))

maior = verifica_maior(A, B)

print(maior)