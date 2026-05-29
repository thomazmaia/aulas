# Crie um programa que peça ao usuário para inserir números interios positivos e adicione-os em uma lista até que ele digite -1 para parar de adicionar números. Em seguida crie uma função para remover um número específico dessa lista. Peça esse número ao usuário e remova-o. Caso não exista, informe ao usuário. Caso exista mais de um, remova apenas o primeiro.

def remover_numero(lista : list, N : int):
    if N in lista:
        lista.remove(N)
    else:
        print("Não está na lista")


lista = []

N = 0
while N != -1:
    N = int(input("Digite um número: "))    
    if N != -1:
        lista.append(N)

print(lista)

N = int(input("Digite um número para remover: "))
remover_numero(lista, N)

print(lista)