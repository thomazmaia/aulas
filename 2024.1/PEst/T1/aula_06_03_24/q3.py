def converter_moeda(valor : float, para_dolar : bool = "True"):
    taxa = 5.30
    if para_dolar:
        return valor / taxa
    else:
        return valor
    

print(f"U$ {converter_moeda(100)}")
print(f"R$ {converter_moeda(100, False)}")