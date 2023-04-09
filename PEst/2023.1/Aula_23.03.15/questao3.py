# 3. Leia uma frase do usuário e diga quantas  palavras essa frase tem.

frase = input("Digite uma frase: ")
qtd_palavras = len(frase.split())
print(f"A frase '{frase}' tem {qtd_palavras} palavras.")
