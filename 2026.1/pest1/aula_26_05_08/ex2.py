# Leia uma frase do usuário e crie uma função para retornar quantas palavras tem mais de 4 letras.
# Ex: "todo mundo odeia o john" -> 2

def conta_letras(frase : str):
    lista = frase.split() # quebrei a frase em palavras
    contador = 0
    for item in lista: # percorri todas as palavras
        if len(item) > 4: # verifique o tamanho da palavra
            contador += 1 # se for maior que 4, conta + 1
    return contador

frase = input("Frase: ")

print(f"A frase: '{frase}' tem {conta_letras(frase)} palavras com mais de 4 letras")
