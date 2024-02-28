# Escreva um código em Python que utilize o laço for para calcular a soma dos quadrados dos números inteiros de 1 a 100 e armazená-la em uma variável chamada 'soma'. Utilize uma única linha de código dentro do laço for.

soma = 0

for i in range (1, 101):
    soma += i ** 2

print(soma)