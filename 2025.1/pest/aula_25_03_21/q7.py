N = int(input("Digite um número de 3 dígitos: "))
N2 = N
# Primeira parte:
d1 = N % 10 # Unidade
N = N // 10 
d2 = N % 10 # Dezena
N = N // 10 
d3 = N % 10 # Centena
N = N // 10 

# Segunda parte:
if d1 == d3:
    print(f"{N2} É um palíndromo!")
else:
    print(f"{N2} NÃO É um palíndromo!")