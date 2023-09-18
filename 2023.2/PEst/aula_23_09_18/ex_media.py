# um aluno tem cinco notas e deseja calcular a
# média aritmética dele

notas = [6, 7, 5, 8, 9]

i = 0
tamanho = 5
soma = 0

while i < tamanho:
    soma = soma + notas[i]
    i += 1

print(f"Média = {soma/tamanho}")
