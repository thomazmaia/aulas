frase = "Um um elefante incomoda muita gente, dois elefantes incomodam, incomodam muito mais!"

lista = frase.lower().replace(",", "").split()
ocorrencia = {}

for palavra in lista:
    if palavra in ocorrencia:
        ocorrencia[palavra] = ocorrencia[palavra] + 1
    else:
        ocorrencia[palavra] = 1

print(ocorrencia)
