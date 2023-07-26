# Função sem retorno e sem argumento
def escreve_menu():
    print("--- CALCULADORA --- ")
    print("[0] - Sair")
    print("[1] - Somar")
    print("[2] - Subtrair")
# Função sem retorno e com argumento
def somar(a , b):
    res = a + b
    print(f"Soma: {res}")
# Função com retorno e com argumento
def subtrair(x, y):
    res = x - y
    return res
# Função com retorno e sem argumento
def leia_opcao():
    num1 = int(input("Digite o numero 1: "))
    num2 = int(input("Digite o numero 2: "))
    return num1, num2


while True:
    escreve_menu()
    op = int(input("Digite uma opção: "))
    if op == 0:
        break

    N1, N2 = leia_opcao()
    
    if op == 1:
        somar(N1, N2)
    elif op == 2:
        resultado = subtrair(N1, N2)
        print(f"Subtração: {resultado}")