def verifica_se_dentro(x, y):
    if ((x >= 2) and (x <= 6)) and ((y >= 3) and (y <= 5)):
        return f"P({x},{y}) está dentro"
    else:
        return f"P({x},{y}) está fora"
    


print(verifica_se_dentro(4,4))
print(verifica_se_dentro(5,4))
print(verifica_se_dentro(6,3))
print(verifica_se_dentro(5.5,5.5))
print(verifica_se_dentro(1,5.5))