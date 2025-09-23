# Crie uma função chamada converter_moeda que aceita um valor em reais e um parâmetro nomeado para_dolar (com valor padrão True). Se para_dolar for True, a função deve converter o valor para dólares (usando uma taxa fictícia) e retornar o valor convertido. Caso contrário, deve retornar o valor original em reais.

def converter_moeda(valor : float, para_dolar : bool = True):
    if para_dolar == True:
        return valor * 5.28
    else:
        return valor
    
res =  converter_moeda(35, True)
print(res)

res = converter_moeda(35, False)
print(res)

res = converter_moeda(35)
print(res)