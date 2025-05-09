# INTRODUÇÃO A LISTAS EM PYTHON
# Listas são um tipo de variável que podem armazenar múltiplos valores. São dispostas entre colchetes [] e seus elementos são separados por vírgulas.
# Exemplo de lista
lista = [1, 2, 3, 4, 5]
print(lista[0])

# Listas podem armazenar diferentes tipos de dados, como números inteiros, strings e até outras listas.
# Exemplo de lista com diferentes tipos de dados
lista = [1, 2, 3, "quatro", "cinco"]
print(lista[0])

# Para acessar um elemento específico da lista, utilizamos o índice do elemento entre colchetes. Lembre-se que os índices começam em 0.
# Exemplo de acesso a elementos da lista
lista = [1, 2, 3, 4, 5]
print(lista[4])  # Acessa o quinto elemento da lista
print(lista[5]) # Acessa o sexto elemento da lista (que não existe, resultando em erro)