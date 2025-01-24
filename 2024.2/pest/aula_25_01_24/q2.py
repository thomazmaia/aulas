L = ['maçã', 'banana', 'laranja', 'uva']

fruta = input("Digite uma fruta: ")

if fruta in L:
    L.remove(fruta)

print(L)