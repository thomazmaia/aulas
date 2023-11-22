# 4. Faça um programa par ler um número N qualquer (positivo ou negativo) do usuário e escreva todos os números de zero até N.

numero = int(input("Número: "))

contador = 0

if numero > 0:
    # Numero positivo
    while contador <= numero:
        print(contador)
        contador += 1   
else:
    # Numero negativo
    while contador >= numero:
        print(contador)
        contador -= 1   