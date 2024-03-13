def eh_par(num : int):
    if num % 2 == 0: #se for par
        return True
    return False



N = int(input("Digite um número: "))

if eh_par(N):
    print(f"{N} é par")
else:
    print(f"{N} é ímpar")