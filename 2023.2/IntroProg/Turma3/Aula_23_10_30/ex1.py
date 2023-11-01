# Leia um número inteiro e verifique se ele é par ou ímpar

numero = int(input("Número: "))

eh_par = numero % 2 == 0

if not (eh_par):
    print("Ímpar")
else:
    print("Par")
