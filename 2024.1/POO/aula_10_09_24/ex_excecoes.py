x = 0
try:
    res = x/0
    print(res)
except ZeroDivisionError:
    print("Erro ao dividir por zero")