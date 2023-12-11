M = int(input("M = "))
N = int(input("N = "))

if M > N:
    menor = N
    maior = M
else:
    menor = M
    maior = N

while menor <= maior:
    if menor % 2 == 0:
        print(menor)
    menor += 1