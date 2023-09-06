def converter_moeda(valor, para_dolar=True):
    taxa = 5.0
    if para_dolar == True:
        novo_valor = valor / taxa
        return novo_valor
    else:
        return valor
    
valor_teste = float(input("Digite um valor: R$"))
novo_valor = converter_moeda(valor_teste)
print(novo_valor)
novo_valor = converter_moeda(valor_teste, "")
print(novo_valor)