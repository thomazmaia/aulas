frase = "Parabens pra voce"

frase = frase.lower().replace(" ", "")

ocorrencia = {}

for letra in frase:
    if letra in ocorrencia:
        ocorrencia[letra] = ocorrencia[letra] + 1
    else:
        ocorrencia[letra] = 1

print(ocorrencia)
