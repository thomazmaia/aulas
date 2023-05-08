cadastro = dict()

for i in range(3):
    nome = input("Digite o nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    cadastro[nome] = idade
print(cadastro)

soma_das_idades = 0
for chave in cadastro.keys():
    soma_das_idades = soma_das_idades + cadastro[chave]

idade_media = soma_das_idades / len(cadastro)

print(f"A idade média desse cadastro é {idade_media}")