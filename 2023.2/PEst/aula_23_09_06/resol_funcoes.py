# 1. Escreva uma função que receba dois números e informe o maior deles.

def questao_1():
    def verifica_maior(num1, num2):
        if num1 > num2:
            print(f"{num1} é o maior")
        elif num2 > num1:
            print(f"{num2} é o maior")


    numero1 = float(input("Digite o 1o número: "))
    numero2 = float(input("Digite o 2o número: "))

    verifica_maior(numero1, numero2)


def questao_2():
    def calcula_menor(num1, num2, num3):
        if num1 <= num2 and num1 <= num3:
            print(f"{num1} é o menor")
        if num2 <= num1 and num2 <= num3:
            print(f"{num2} é o menor")
        if num3 <= num2 and num3 <= num1:
            print(f"{num3} é o menor")                        

    numero1 = float(input("Digite o 1o numero: "))
    numero2 = float(input("Digite o 2o numero: "))
    numero3 = float(input("Digite o 3o numero: "))

    calcula_menor(num2=numero2, num1=numero1, num3=numero3)


questao_1()