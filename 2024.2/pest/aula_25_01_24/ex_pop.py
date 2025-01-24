# REMOVER ELEMENTOS - pop()
# -> Remove um elemento em uma posição específica (ou no final)
L = [3, 5, 10, 4, 3, 8, 5, 0]
print(f"Lista antes: {L}")
L.pop(5) # Remove o elemento índice 5
print(f"Lista depois: {L}")
L.pop() # Remove o último elemento
print(f"Lista depois: {L}")