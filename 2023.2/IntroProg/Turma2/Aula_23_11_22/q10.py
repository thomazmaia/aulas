# 10. Modifique o programa anterior para dar “pistas” ao usuário informando se o número que ele digitou é menor ou maior que o número secreto pré-definido.
from random import randint

numero_secreto = randint(1, 100)

numero_usuario = int(input("Digite um número: "))

while numero_usuario != numero_secreto:
    print("Número errado!")
    if numero_usuario > numero_secreto:
        numero_usuario = int(input("Digite um número MENOR: "))
    else:
        numero_usuario = int(input("Digite um número MAIOR: "))

print("Você acertou!")