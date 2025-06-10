def saltos(s : str, passo : int):
    nova_string = s[::passo]
    return nova_string

print(saltos("Eu gosto de abacaxi", 3))