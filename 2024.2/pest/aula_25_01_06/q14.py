def reverter(entrada : str):
    invertida = entrada[-1: -len(entrada)-1 :-1]
    return invertida

def inverter_direita(str : str):
    tamanho_da_string = len(str)
    metade = int(tamanho_da_string/2)
    primeira_metade = str[0:metade]
    segunda_metade = str[metade:]
    nova_str = primeira_metade + reverter(segunda_metade)
    return nova_str

print(inverter_direita("Pythonista"))