def inverte_string(str):
    nova_str = str[::-1]
    return nova_str


str_original = "Python"
str_invertida = inverte_string(str_original)


print(f"String original: {str_original}")
print(f"String invertida: {str_invertida}")