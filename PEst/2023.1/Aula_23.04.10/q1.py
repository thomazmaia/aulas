# 1. Escreva uma função para verificar um número é par ou ímpar.

def eh_par_ou_impar(numero):
    res = 0
    if numero % 2 == 0:
        res = 'par'
    else:
        res = 'ímpar'
    return res

print(eh_par_ou_impar(2))