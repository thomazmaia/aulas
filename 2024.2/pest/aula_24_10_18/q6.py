# 6. Crie um programa para ler um número de 5 dígitos e verificar se existe algum dígito que se repete 2 ou mais vezes.
# OBS: NÃO converta N para string. Trate-o como número!

numero = int(input("Digite um número de 5 dígitos: "))

# Unidade
dig1 = numero % 10
numero = numero // 10

# Dezena
dig2 = numero % 10
numero = numero // 10

# Centena
dig3 = numero % 10
numero = numero // 10

# Milhar
dig4 = numero % 10
numero = numero // 10

# Dezena de milhar
dig5 = numero % 10

if (dig1 == dig2) or (dig1 == dig3) or (dig1 == dig4) or (dig1 == dig5):
    print(f"{dig1} se repete")

if (dig2 == dig1) or (dig2 == dig3) or (dig2 == dig4) or (dig2 == dig5):
    print(f"{dig2} se repete")

if (dig3 == dig2) or (dig3 == dig1) or (dig3 == dig4) or (dig3 == dig5):
    print(f"{dig3} se repete")

if (dig4 == dig2) or (dig4 == dig3) or (dig4 == dig1) or (dig4 == dig5):
    print(f"{dig4} se repete")

if (dig5 == dig2) or (dig5 == dig3) or (dig5 == dig4) or (dig5 == dig1):
    print(f"{dig5} se repete")
