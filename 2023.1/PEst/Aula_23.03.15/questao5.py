# 5.  Leia uma frase do usuário e divida a frase em palavras. Mostre todas as palavras em minúsculas mas com a última letra maiúscula.

frase = input("Digite uma frase: ")
palavras = frase.split()
for palavra in palavras:
    print(palavra[:-1].lower() + palavra[-1].upper())
