# Desenvolva um programa para ajudar um restaurante a calcular a gorjeta a ser dada
# ao garçom. Peça ao usuário para inserir o valor total da conta e, em seguida, com
# base em sua satisfação, permita que o usuário escolha uma porcentagem de gorjeta
# (10%, 15% ou 20%). Calcule e exiba o valor da gorjeta.

valor_conta = float(input("Valor total da conta: "))

gorjeta = int(input("Gorjeta (10%, 15% ou 20%): "))

if gorjeta == 10:
    valor_a_mais = (10 / 100) * valor_conta
if gorjeta == 15:
    valor_a_mais = (15 / 100) * valor_conta
if gorjeta == 20:
    valor_a_mais = (20 / 100) * valor_conta

print(f"Gorjeta: R${valor_a_mais}")
nova_conta = valor_conta + valor_a_mais
print(f"Nova conta: R${nova_conta}")
