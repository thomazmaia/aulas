
N = 0
soma = 0
quantidade = 0

while N != -1:
    N = int(input("Digite um número: "))
    if N != -1:
        soma += N
        quantidade += 1

print("saiu...")
print(f"A soma deu {soma}")
print(f"A quantidade deu {quantidade}")
print(f"A média deu {soma/quantidade}")