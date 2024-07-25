def inverte_string(string : str):
    nova_string = string[::-1]
    return nova_string


minha_string = "Python"
string_invertida = inverte_string(minha_string)

print(f"String original: {minha_string}")
print(f"String invertida: {string_invertida}")