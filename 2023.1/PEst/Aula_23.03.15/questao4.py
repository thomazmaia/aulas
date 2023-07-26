# 4. Leia uma frase do usuário e divida a frase em palavras. Mostre todas as palavras  em maiúsculas.

frase = input("Digite uma frase: ")
palavras = frase.split()
for palavra in palavras:
    print(palavra.upper())
