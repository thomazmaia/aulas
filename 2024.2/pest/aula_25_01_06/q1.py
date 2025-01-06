def primeiro_e_ultimo(str_qualquer : str):
    primeiro_caractere = str_qualquer[0]
    ultimo_caractere = str_qualquer[-1]
    nova_string = primeiro_caractere + ultimo_caractere
    return nova_string


print(primeiro_e_ultimo("Python"))