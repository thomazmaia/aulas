# Parte 0: leitura do número
N = int(input("Digite um número qualquer: "))
N_copia = N

# Parte 1: contagem da quantidade de dígitos
qtd_digitos = 0

while N != 0:
    N = N // 10
    qtd_digitos += 1

print(f"Esse número tem {qtd_digitos} dígitos")

# Parte 2: cálculo da soma dos dígitos elevado à potência (quantidade de dígitos)
N = N_copia

soma = 0
while N != 0:
    digito = N % 10
    N = N // 10
    soma = soma + (digito ** qtd_digitos)

print(f"A soma dos dígitos foi de {soma}")

# Parte 3: verifica se é ou não número de armstrong
if soma == N_copia:
    print("O número É um número de Armstrong")
else:
    print("O número NÃO É um número de Armstrong")