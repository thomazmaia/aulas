# ----------------------------------------------
# 01 - O volume de uma esfera com raio r é dado por 4/3pir3. Qual o volume de uma esfera com raio 5?
# OBS: inicie a variável r com o valor 5.
# ----------------------------------------------
raio = 5
pi = 3.14

vol = 4/3 * pi * raio ** 3
print(f"O volume da esfeera de raio {raio} é {vol}.")
# ----------------------------------------------
# 02 - Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias.
# ----------------------------------------------
qtd_de_livros = 60
capa = 24.95
desconto = 40/100
transporte_1 = 3
transporte_2 = 0.75

# Valor dos livros com desconto
novo_preco = capa - desconto*capa
valor_livros = qtd_de_livros * novo_preco

# Valor do transporte
valor_transporte = (qtd_de_livros - 1) * transporte_2 + transporte_1

# Valor total
valor_total = valor_livros + valor_transporte

print(f"O valor da compra de {qtd_de_livros} é R$ {valor_total} sendo dividido R$ {valor_livros} de livros e R$ {valor_transporte} de transporte dos {qtd_de_livros} livros.")
# ----------------------------------------------
# 03 - Você olha para um relógio e são exatamente 2 da tarde. Você coloca um alarme para tocar daqui a 51 horas. A que horas o alarme irá tocar?
# OBS: desconsidere minutos e segundos
# ----------------------------------------------
hora = 14
alarme = 51

nova_hora = hora + (alarme % 24)

print(f"São {hora} horas e daqui a {alarme} horas será {nova_hora} horas.")
# ----------------------------------------------
# 04 - Escreva um programa em Python que resolve a versão geral do problema acima. Peça ao usuário que entre com a hora atual (em horas) e que entre com o número de horas que deverá esperar antes do alarme tocar. Seu programa deve imprimir a hora que o alarme irá tocar.
# ----------------------------------------------
hora = int(input("Que horas são agora: "))
alarme = int(input("Qual a duração do alarme: "))

nova_hora = hora + (alarme % 24)

print(f"São {hora} horas e daqui a {alarme} horas será {nova_hora} horas.")
# ----------------------------------------------
# 05 - Escreva um programa para ler um número N e mostre N, NN e NNN. • Ex: para N = 5, mostre: 5, 55, 555
# ----------------------------------------------
N = int(input("Digite o número: "))
NN = N * 10 + N
NNN = NN * 10 + N
print(N, NN, NNN)
# ----------------------------------------------
# 06 - Crie um programa para calcular a área de um triângulo dado o valor da base e da sua altura.
# ----------------------------------------------
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area_tri = (base * altura) / 2

print(f"A área do triângulo de base {base} e altura {altura} é {area_tri}.")
# ----------------------------------------------
# 07 - Escreva um programa para resolver (x + y) * (x + y).
# ----------------------------------------------
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

res = (x + y) * (x + y)

print(f"O resultado é {res}.")
# ----------------------------------------------
# 08 - Crie um programa para calcular a distância entre os pontos (x1, y1) e (x2,y2).
# ----------------------------------------------
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

res = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1/2

print(f"A distância entre os dois pontos é {res}")
# ----------------------------------------------
# 09 - Escreva um programa para converter distância de metros para pés, polegadas e milhas.
# ----------------------------------------------
dist = float(input("Digite o valor em metros a ser convertido: "))
pes = dist * 3.28
pol = dist * 39.37
mil = dist * 0.62/1000

print(f"{dist} metros equivale a {pes} pés")
print(f"{dist} metros equivale a {pol} polegadas")
print(f"{dist} metros equivale a {mil} milhas")
# ----------------------------------------------
# 10 - Escreva um programa para calcular a soma dos dígitos de um número de 4 dígitos.
# Ex: para N = 5928, mostre: 24
# ----------------------------------------------
N = int(input("Digite um número de 4 dígitos: "))

dig_4 = N % 10
novo_N = N // 10

dig_3 = novo_N % 10
novo_N = novo_N // 10

dig_2 = novo_N % 10
novo_N = novo_N // 10

dig_1 = novo_N % 10

res = dig_1 + dig_2 + dig_3 + dig_4

print(f"A soma dos dígitos de {N} é {res}.")