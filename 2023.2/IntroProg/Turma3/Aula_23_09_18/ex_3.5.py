# Calcule o resultado da expressão A > B and C or D,
# utilizando os valores da tabela a seguir.
#  A  B  C      D      Resultado
#  1  2  True   False
# 10  3  False  False
#  5  1  True   True
A = 1
B = 2
C = True
D = False
res = A > B and C or D
print(res)


A = 10
B = 3
C = False
D = False
res = A > B and C or D
print(res)

A = 5
B = 1
C = True
D = True
res = A > B and C or D
print(res)
