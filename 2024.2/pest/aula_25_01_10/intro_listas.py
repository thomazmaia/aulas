# INTRODUÇÃO A LISTAS
# Listas são sequências de elementos acessados por índices crescentes (iniciados em zero) e separados por vírgula. A lista é declarada entre colchetes []
# Ex: L = ['c', 1, 3.5, 'uva', True]
#     L[0] é a string 'c'
#     L[1] é o inteiro 1
#     L[2] é o decimal 3.5
#     L[3] é a string 'uva'
#     L[4] é o booleano True

# Ex: Crie um código para printar na tela todos os elementos da lista L.
L = ['c', 1, 3.5, 'uva', True]

tamanho_da_lista = len(L)

for i in range(0, tamanho_da_lista, 1):
    print(L[i])