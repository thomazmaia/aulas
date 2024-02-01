# Ex: Programa para calcular o fatorial de um número dado pelo usuário e mostrar a quantidade de multiplicações feitas

# Solicitar ao usuário um número para calcular o fatorial
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1 # Inicializar o fatorial como 1
mult = 0 # Inicia a quantidade de multiplicações  com zero

# Enquanto o número for maior que 1
while numero >= 1:
    # Multiplicar o fatorial pelo número atual
    fatorial *= numero
    # Decrementar o número
    numero -= 1
    mult += 1

# Imprimir o fatorial calculado
print("O fatorial é:", fatorial)
# Contagem de multiplicações
# mult = mult - 1
print(f"Foram feitas {mult - 1} multiplicações")