# FATIAMENTO (SLICING) DE LISTAS
# Ex em strings:
# fruta = 'ABACAXI'
# print(fruta[0:3]) # ABA
# print(fruta[3:])  # CAXI
#
# Ex em listas:
# lista = ['uva', 'maça', 'limão', 'laranja', 'morango']
# print(lista[0:3])
#
# Relembrando:
# lista[inicio:fim:passo]

notas = ['uva', 6, 'dez', True, 'aaa', 'oi', '9.5', 'casa', 6.2, 4.9]
print(notas[0:7:2])

print(notas[-1     :   -len(notas)-1   :    -1])