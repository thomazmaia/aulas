def eh_positivo(numero : float):
    if numero > 0:
        return True
    return False

def eh_negativo(numero : float):
    if numero < 0:
        return True
    return False

def eh_zero(numero : float):
    if numero == 0:
        return True
    return False


# Função SEM RETORNO
def verifica_numero(numero : float):
    if eh_positivo(numero):
        print("Número positivo")
    elif eh_negativo(numero):
        print("Número negativo")
    elif eh_zero(numero):
        print("Número zero")

while True:
    N = float(input("Digite um número: "))
    verifica_numero(N)