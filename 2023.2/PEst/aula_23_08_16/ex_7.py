N = int(input("Digite um número de 3 dígitos: "))

D1 = N // 100
D3 = N % 10

if D1 == D3:
    print("Palindromo")
else:
    print("Não é palindromo")
