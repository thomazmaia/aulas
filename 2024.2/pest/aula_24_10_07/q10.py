# 10. Escreva um programa para calcular a soma dos dígitos de um número de 4 dígitos.
# Ex: para N = 5928, mostre: 24

N = 1234
unidade = N % 10

N = N // 10
dezena = N % 10

N = N // 10
centena = N % 10

N = N // 10
milhar = N


print(milhar)
print(centena)
print(dezena)
print(unidade)

soma = milhar + centena + dezena + unidade
print(soma)