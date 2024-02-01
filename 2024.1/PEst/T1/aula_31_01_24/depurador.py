N1 = float(input("Digite a nota 1: "))
N2 = float(input("Digite a nota 2: "))
N3 = float(input("Digite a nota 3: "))

media = (N1 + N2 + N3)/3

if media >= 6:
    print(f"Aprovado com média {media}")
else:
    print(f"Reprovado com média {media}")