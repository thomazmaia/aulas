# 2. Crie uma função chamada `intervalo` que receba uma string e dois índices (int) como parâmetros de entrada e retorne a substring que está entre esses dois índices, incluindo o caractere no primeiro índice, mas excluindo o caractere no último índice.
# Ex: 'intervalo(”Python”, 1, 4)' deve retornar a substring “yth”

def intervalo(str : str, id1 : int, id2 : int):
    return str[id1:id2]

print(intervalo("Python", 3, 5))