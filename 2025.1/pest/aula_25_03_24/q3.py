num = int(input("Digite um número: "))

soma = 0

for i in range(0, num+1, 2):
    #print(i)
    soma = soma + i

print(f"A soma foi: {soma}")