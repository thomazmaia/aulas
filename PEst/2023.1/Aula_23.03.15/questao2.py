# 2. Leia uma palavra do usuário e informe qual a primeira letra e a última letra da palavra.

palavra = input("Digite uma palavra: ")
primeira_letra = palavra[0]
ultima_letra = palavra[-1]
print(f"A primeira letra da palavra '{palavra}' é '{primeira_letra}' e a última letra é '{ultima_letra}'.")