# Crie uma função que receba uma string (informada pelo usuário) e retorne a mesma string com o primeiro caractere modificado. O primeiro caractere a string deve ser um zero. Ao final, mostre a string resultante.
# Ex:
# "Abacaxi" vira "0bacaxi"

def troca_caractere(palavra : str):
    res = "0" + palavra[1::]
    return res

fruta = input("Digite uma fruta: ")
print(troca_caractere(fruta))