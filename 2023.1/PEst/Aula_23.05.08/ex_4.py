cadastro = dict()

for i in range(3):
    nome = input("Digite o nome: ")
    idade = input(f"Digite a idade de {nome}: ")
    cadastro[nome] = idade
print(cadastro)

for chave, valor in cadastro.items():
    print(f"Nome: {chave} -- Idade: {valor}")