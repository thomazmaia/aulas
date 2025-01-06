def trocar_metades(str : str):
    tamanho_da_string = len(str)
    metade = int(tamanho_da_string/2)
    primeira_metade = str[0:metade]
    segunda_metade = str[metade:]
    nova_str = segunda_metade + primeira_metade
    return nova_str


print(trocar_metades("Abacaxi"))