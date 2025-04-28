def eh_par(numero : int):
    if numero % 2 == 0:
        return True
    else:
        return False


N = int(input("Digite um número: "))

if eh_par(N) == True:
    print(f"{N} é par")
else:
    print(f"{N} é ímpar")