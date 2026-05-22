# LISTAS
# São estruturas de dados que armazenam valores em elementos que são acessados por um índice (semelhante às strings) e são separados por virgula. Uma lista pode conter zero ou mais elementos e o tamanho dessa lista é dado pela quantidade de elementos contidos nela.
# Ex:
# L = [1, 2, 3]
# len(L) -> 3
# L[0] -> 1

# Grande diferença entre strings e listas: listas são MUTÁVEIS
S = "abc"
print(S[0])
#S[0] = "@" # ERRO

L =[1, 2, 3]
print(L[0])
L[0] = 99

print(L)

# Acessando os elementos da lista
L = [1, 2, 3, 3.2, 6.17, 'A', 'B', 'Abacaxi', True]

print(L)
for indice in range(len(L)):
    print(L[indice])

print(L)
for item in L:
    print(item)