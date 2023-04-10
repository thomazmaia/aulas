# 7. Escreva uma função que receba uma lista contendo as notas de um aluno e um número que representa o valor da média para ser aprovado. A função deve retornar a situação do aluno: aprovado ou reprovado. Caso o usuário não coloque nenhum número, sua função deve adotar 7 como valor padrão.

def verifica_se_passou(lista, media=7):
    soma = 0
    for item in lista:
        soma = soma + item
    quantidade = len(lista)

    minha_media = soma/quantidade

    if minha_media >= media:
        return "Aprovado"
    else:
        return "Reprovado"

print( verifica_se_passou([10, 6, 8]) )
print( verifica_se_passou([7, 7, 4], 6) )
print( verifica_se_passou([7, 6, 5, 7]) )
print( verifica_se_passou([4.5, 9.3, 7.8, 8]) )