# Escreva um programa que use as funções adicionar_elemento e remover_elemento para
# transformar a lista frutas na lista frutas_desejadas de acordo com as seguintes
# etapas:
# - Inicialmente, frutas contém ['maçã', 'banana', 'uva', 'laranja'].
# - Adicione 'morango' no final da lista.
# - Remova 'uva' da lista.
# - Adicione 'abacaxi' na posição 1 (índice 1) da lista.
# Lembre-se de imprimir frutas_desejadas no final do seu programa.


def adicionar_elemento(lst, indice, elemento):
    if indice == "final":
        lst.append(elemento)
    else:
        lst.insert(indice, elemento)


def remover_elemento(lst, elemento):
    if elemento in lst:
        lst.remove(elemento)


frutas = ["maçã", "banana", "uva", "laranja"]
print(f"Frutas antes: {frutas}")
adicionar_elemento(frutas, "final", "morango")
remover_elemento(frutas, "uva")
adicionar_elemento(frutas, 1, "abacaxi")
frutas_desejadas = frutas[:]
print(frutas_desejadas)
