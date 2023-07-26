lista_de_frutas = ["abacaxi", "laranja", "maca", "ata", "ameixa", "limao"]

res = ()

for fruta in lista_de_frutas:
    if fruta[0] in "aA":
        if fruta not in res:
            res += tuple([fruta])

print(res)
