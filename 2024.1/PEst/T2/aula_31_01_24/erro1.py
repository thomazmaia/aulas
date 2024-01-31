# Ex: Programa para calcular a soma dos números pares até um número limite dado pelo usuário

limite = input("Digite um número limite: ") # Solicitar ao usuário um número limite
limite = int(limite) # Converter o input para um número inteiro
soma = 0 # Inicializar a variável para armazenar a soma
numero = 0 # Inicializar o número

# Enquanto o número for menor ou igual ao limite
while numero <= limite:
    # Verificar se o número é par
    if numero % 2 == 0:
        # Adicionar o número à soma
        soma += numero
    # Incrementar o número
    numero += 1

# Imprimir a soma dos números pares
print(f"A soma dos números pares até {limite} é {soma}")
