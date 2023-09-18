# um aluno tem cinco notas e deseja calcular a
# média aritmética dele. leia as notas do aluno

notas = [0, 0, 0, 0, 0]

i = 0
tamanho = 5

while i < tamanho:
    notas[i] = float(input("Digite a nota: "))
    i += 1

i = 0
soma = 0
while i < tamanho:
    soma += notas[i]
    i += 1

print(f"Média: {soma/tamanho}")
