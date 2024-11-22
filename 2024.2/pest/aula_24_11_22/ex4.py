# Crie uma função que receba dois números e esceva na tela quem é o maior e quem é o menor número. Caso sejam iguais, escreva "são iguais"

def verifica_maior_menor(num1 : float, num2 : float):
    if num1 > num2:
        print(f"Maior: {num1}")
        print(f"Menor: {num2}")
    elif num2 > num1:
        print(f"Maior: {num2}")
        print(f"Menor: {num1}")
    else:
        print("Números iguais")


verifica_maior_menor(0, 0)