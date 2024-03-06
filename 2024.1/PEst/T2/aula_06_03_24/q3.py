# Crie uma função chamada converter_moeda que aceita um valor em reais e um parâmetro nomeado para_dolar (com valor padrão True). Se para_dolar for True, a função deve converter o valor para dólares (usando uma taxa fictícia) e retornar o valor convertido. Caso contrário, deve retornar o valor original em reais.

def converter_moeda(valor_rs : float, para_dolar : bool = True):
    taxa = 5.30
    if para_dolar == True:
        return valor_rs / taxa
    else:
        return valor_rs


U = converter_moeda(100)
R = converter_moeda(100, False)

print(f"U$ {U}")
print(f"R$ {R}")