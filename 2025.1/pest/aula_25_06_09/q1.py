def primeiro_e_ultimo(s : str):
    primeiro = s[0]
    ultimo = s[len(s)-1]
    nova_string = primeiro + ultimo
    return nova_string

print(primeiro_e_ultimo("caixa"))