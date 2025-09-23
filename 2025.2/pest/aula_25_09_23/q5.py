# Defina uma função chamada contagem_regressiva que aceita um número inteiro positivo como parâmetro e imprime uma contagem regressiva a partir desse número até zero.

def contagem_regressiva(num : int):
    for i in range(num, -1, -1):
        print(i)


contagem_regressiva(10)
contagem_regressiva(5)
contagem_regressiva(13)
contagem_regressiva(20)