def maior_menor(tupla):
    maior = tupla[0]
    menor = tupla[0]

    for item in tupla:
        if item > maior:
            maior = item
        if item < menor:
            menor = item
    return maior, menor


tupla = (10, 5, -3, 20, 8)
maior, menor = maior_menor(tupla)
print(f"Maior = {maior}")
print(f"Menor = {menor}")
