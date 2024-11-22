# Crie uma função que receba dois números e retorne o maior deles.

def verifica_maior(num1, num2):
    if num1 > num2:
        maior = num1
    elif num2 > num1:
        maior = num2
    else:
        maior = num1
    return maior

aux = verifica_maior(10, 10)
print(aux)