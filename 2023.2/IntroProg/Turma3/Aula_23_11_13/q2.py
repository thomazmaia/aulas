# Escreva um programa para verificar se um aluno do IF passou sabendo que ele fez 5 provas mas a menor e a maior nota são descartadas. É feita a média aritmética com as notas restantes para gerar a média parcial (MP). Caso a MP seja pelo menos 6 o aluno passa direto. Caso seja inferior a 3 o aluno reprova direto. Caso seja entre 3 e 6 o aluno está de recuperação.

N1 = float(input("Nota 1: "))
N2 = float(input("Nota 2: "))
N3 = float(input("Nota 3: "))
N4 = float(input("Nota 4: "))
N5 = float(input("Nota 5: "))

# Pega o maior
if N1 >= N2 and N1 >= N3 and N1 >= N4 and N1 >= N5:
    maior = N1
if N2 >= N1 and N2 >= N3 and N2 >= N4 and N2 >= N5:
    maior = N2
if N3 >= N1 and N3 >= N2 and N3 >= N4 and N3 >= N5:
    maior = N3
if N4 >= N1 and N4 >= N2 and N4 >= N3 and N4 >= N5:
    maior = N4
if N5 >= N1 and N5 >= N2 and N5 >= N3 and N5 >= N4:
    maior = N5
# Pega o menor
if N1 <= N2 and N1 <= N3 and N1 <= N4 and N1 <= N5:
    menor = N1
if N2 <= N1 and N2 <= N3 and N2 <= N4 and N2 <= N5:
    menor = N2
if N3 <= N1 and N3 <= N2 and N3 <= N4 and N3 <= N5:
    menor = N3
if N4 <= N1 and N4 <= N2 and N4 <= N3 and N4 <= N5:
    menor = N4
if N5 <= N1 and N5 <= N2 and N5 <= N3 and N5 <= N4:
    menor = N5

MP = (N1 + N2 + N3 + N4 + N5 - maior - menor)/3
print(f"Média parcial: {MP}")

if MP >= 6:
    print("Passou")
elif MP < 3:
    print("Reprovou")
else:
    print("Recuperação")