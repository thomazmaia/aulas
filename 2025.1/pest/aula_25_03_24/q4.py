N = int(input("Digite um número: "))

soma = 0

for i in range(N+1):
    soma += i

print(f"A soma foi: {soma}")

media = soma/(N+1)

print(f"A média foi: {media}")
