# Crie uma função que receba um número como parâmetro, verifique e retorne se um número é positivo, negativo ou nulo/zero.

def eh_zero(N : float):
    if N == 0:
        return True
    return False

def eh_positivo(N : float):
    if N > 0:
        return True
    return False

def eh_negativo(N : float):
    if N < 0:
        return True
    return False

def verifica_numero(N : float):
    if eh_zero(N):
        return "Nulo"
    elif eh_positivo(N):
        return "Positivo"
    elif eh_negativo(N):
        return "Negativo"

# PROGRAMA PRINCIPAL
N = float(input("N = "))
print(verifica_numero(N))