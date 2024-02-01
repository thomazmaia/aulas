# Ex: Programa para verificar se um número é primo

# Solicitar ao usuário um número para verificar se é primo
numero = int(input("Digite um número: "))
divisores = 0 # Inicializar o contador de divisores
contador = 2

# Enquanto o contador for menor que o número
while contador < numero:
    # Verificar se o número é divisível pelo contador atual
    if numero % contador == 0:
        # Se for divisível, incrementar o contador de divisores
        divisores += 1
    contador += 1 # Incrementar o contador

# Verificar se o número de divisores é igual a zero
if divisores == 0:
    print(numero, "é primo!")
else:
    print(numero, "não é primo!")