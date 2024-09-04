notas = {
    'Arthur' : [8.4, 6, 5.9],
    'Andrew' : [7.0, 6.3, 8.1],
    'Willame' : [4.5, 3.0, 9.5]
}

nome = input("Digite o nome: ")

print(notas[nome])

lista_de_notas = notas[nome]
soma = 0
for nota in lista_de_notas:
    soma += nota
print(soma/3)