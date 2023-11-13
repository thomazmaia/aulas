string = "Hora do ALMOÇO"

# Maiúscula e miníscula
print(string)
NOVA = string.upper()
nova = string.lower()
print(NOVA)
print(nova)

# Separação
aux = string.split()
print(aux)


# Crie um código para ler uma FRASE e transforme essa frase em uma outra frase completamente MAIÚSCULA e sem espaços.
# Ex: hoje é um bom dia
#     HOJEÉUMBOMDIA

frase = input("Frase: ").upper()
lista = frase.split()

aux = ''

for item in lista:
    aux = aux + item

print(aux)