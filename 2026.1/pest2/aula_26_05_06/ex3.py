# Crie uma função chamada "intervalo" que receba uma string e dois inteiros (int) como parâmetros de entrada e retorne a substring que está entre esses dois índices (incluindo o caractere no primeiro índice e excluindo o caractere no segundo índice).
# Ex:
# intervalo("Abacaxi", 1, 5) -> "baca"

def intervalo(string : str, num1 : int, num2 : int):
    substring = string[num1 : num2]
    return substring

print(intervalo("1234567890xi", 1, 5))