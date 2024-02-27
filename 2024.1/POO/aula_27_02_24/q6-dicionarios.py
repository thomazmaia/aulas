import random

def ver_matriz(matriz):
    qtd_linhas = len(matriz)
    for linha in range(qtd_linhas):
        qtd_colunas = len(matriz[linha])
        for coluna in range(qtd_colunas):
            elemento = matriz[linha][coluna]
            print(f"{elemento: ^3}", end=' ')
        print()

def histograma(matriz):
    dict = {}
    for i in range(16):
        dict[i] = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            dict[matriz[i][j]] += 1
    return dict

def get_valor(valor, hist):
    return hist[valor]

def desenha_histograma(hist):
    for i in range(len(hist)):
        qtd = get_valor(i, hist)
        print(f"{i: >2}: ", end=' ')
        for j in range(qtd):
            print('*', end='')
        print('')


M = int(input("M: "))
N = int(input("N: "))

# Criar a matriz de M x N
matriz = []
for i in range(M):
    linha = []
    for j in range (N):
        valor = random.randint(0, 15)
        linha.append(valor)
    matriz.append(linha)

ver_matriz(matriz)
desenha_histograma(histograma(matriz))