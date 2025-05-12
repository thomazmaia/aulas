# 1 - Crie uma FUNÇÃO que receba uma lista de notas de um aluno e RETORNE a média desse aluno. Teste com as seguintes notas:
# notas = [7, 7.5, 8, 10, 5.5]

def calcular_media(lista_de_notas : list):
    soma = 0
    for nota in lista_de_notas:
        soma = soma + nota

    media = soma/len(lista_de_notas)
    return media


notas = [7, 7.5, 8, 10, 5.5]
media = calcular_media(notas)
print(media)