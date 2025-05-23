# MÉTODOS DE LISTAS

# append() - Adiciona um elemento ao final da lista
frutas = ['uva', 'maca', 'abacaxi']
frutas.append('banana')

# insert() - Adiciona um elemento em uma posição específica
frutas = ['uva', 'maca', 'abacaxi']
frutas.insert(1, 'banana')

# remove() - Remove o item com o valor especificado
frutas = ['uva', 'maca', 'abacaxi']
    # frutas.remove('banana') # erro
if 'uva' in frutas:
    frutas.remove('uva')

# pop() - Remove o elemento em uma posição especificada 
frutas = ['uva', 'maca', 'abacaxi']
frutas.pop(0)

# clear() - Remover todos os elementos da lista
frutas = ['uva', 'maca', 'abacaxi']
frutas.clear()

# copy() - Retorna uma cópia da lista
frutas = ['uva', 'maca', 'abacaxi']
    #frutas2 = frutas # Não cria cópia
frutas2 = frutas.copy()
frutas.remove('uva')

# count() - Retorna o número de elementos com um valor especificado
numeros = [1, 3, 5, 7, 2, 3, 4, 6, 7, 2, 3, 1, 0, 9, 10, 2, 6]
qtd = numeros.count(2)
# print(f"O número 2 aparece {qtd} vezes")

# index() - Retorna um índice da primeira ocorrência de um elemento especificado
numeros = [1, 3, 5, 7, 2, 3, 4, 6, 7, 2, 3, 1, 0, 9, 10, 2, 6]
id = numeros.index(7)
print(f"O número 7 está no índice {id}")

# reverse() - Inverte a ordem da lista
frutas = ['uva', 'maca', 'abacaxi']
frutas.reverse()
# print(frutas)

# extend() - Adiciona os elementos de uma lista ao final da lista atual
numeros = [1, 3, 5, 7, 2, 3, 4, 6, 7, 2, 3, 1, 0, 9, 10, 2, 6]
frutas = ['uva', 'maca', 'abacaxi']
frutas.extend(numeros)
print(frutas)
print(numeros)