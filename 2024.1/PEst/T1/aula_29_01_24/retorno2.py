num_termos = int(input("Quantos termos? "))

n1 = 0
n2 = 1
cont = 0

if num_termos == 1:
    print(n1)
else:
    while cont < num_termos:
        print(n1)
        prox = n1 + n2
        n1 = n2
        n2 = prox
        cont += 1