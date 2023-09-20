# Conversão de Moeda: Crie um programa que converta dólares (U$) em reais
# (R$). Solicite ao usuário o valor em dólares e faça a conversão,
# em seguida, imprima o valor em reais.
# OBS: verificar a cotação do dia.

valor_dolar = float(input("Digite o valor em dólares: "))

valor_real = valor_dolar * 4.85

print(f"U${valor_dolar} equivalem a R${valor_real}")
