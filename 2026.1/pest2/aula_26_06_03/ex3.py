# Crie um programa que peça ao usuário para inserir números interios positivos e adicione-os em uma lista até que ele digite -1 para parar de adicionar números. Em seguida crie uma função para remover um número específico dessa lista. Peça esse número ao usuário e remova-o. Caso não exista, informe ao usuário. Caso exista mais de um, remova apenas o primeiro.

def remove_numero(L : list, N : int):
    if N in list:
        L.remove(N)
    else:
        print(f"{N} não está na lista")


lista = []
while True:
    numero = int(input("Digite um numero: "))
    if numero == -1:
        break
    lista.append(numero)

print(lista)
novo_numero = int(input("Digite o número para remover: "))
remove_numero(lista, novo_numero)
print(lista)