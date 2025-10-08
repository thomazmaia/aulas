# Percorrendo elementos
notas_thai = [2, 4, 10, 4]

qtd_de_elementos = len(notas_thai) # tamanho da lista

for i in range(qtd_de_elementos):
    print(notas_thai[i])


# Exercício: crie um código para calcular a média aritmética das notas da Thainara.
soma = 0
for i in range(qtd_de_elementos):
    soma = soma + notas_thai[i]

media = soma/qtd_de_elementos

print(f"A média da Thainara foi {media}")

if media >= 6:
    print("Passou")
else:
    print("Reprovou")