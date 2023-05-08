cadastro = dict()

for i in range(5):
    nome = input("Digite o nome: ")
    pontos = int(input(f"Digite a pontuação de {nome}: "))
    cadastro[nome] = pontos
print(cadastro)

soma_dos_pontos = 0
for chave in cadastro.keys():
    soma_dos_pontos = soma_dos_pontos + cadastro[chave]

media_dos_pontos = soma_dos_pontos / len(cadastro)

print(f"A idade média desse cadastro é {media_dos_pontos}")