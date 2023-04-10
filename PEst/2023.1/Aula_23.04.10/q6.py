# 6. Escreva uma função que receba uma lista contendo as notas de um aluno e retorne sua média aritmética.

def calc_media(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    quantidade = len(lista)
    return soma/quantidade

print( calc_media([4.5, 9.3, 7.8, 8]) )
print( calc_media([10]) )
print( calc_media([7, 7, 4]) )

