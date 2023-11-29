texto = input("Frase ou palavra: ")

tamanho = len(texto)

print(f"Tamanho = {tamanho}")

texto_min = texto.lower()

contador = 0
novo_texto = ''
for caractere in texto_min:
    if caractere in 'aeiou':
        contador += 1
        novo_texto += '*'
    else:
        novo_texto += caractere

print(f"Vogais = {contador}")
print(novo_texto)

novo_texto = input("Novo texto: ")
novo_texto_reverso = novo_texto[::-1]
if novo_texto == novo_texto_reverso:
    print("Palíndromo")
else:
    print("NÃO Palíndromo")