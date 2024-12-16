def primeiro_e_ultimo(string : str):
    primeiro = string[0]
    tamanho_da_string = len(string)
    ultimo = string[tamanho_da_string-1]
    # ultimo = string[-1] # Último caractere da string
    aux = primeiro + ultimo
    return aux



nova_string = primeiro_e_ultimo('TesteX')
print(nova_string)