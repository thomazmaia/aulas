def reverter(entrada : str):
    invertida = entrada[-1: -len(entrada)-1 :-1]
    return invertida

def palindromo_simples(string : str):
    str_reversa = reverter(string)
    if string == str_reversa:
        return True
    else:
        return False


print(palindromo_simples("roma é amor"))