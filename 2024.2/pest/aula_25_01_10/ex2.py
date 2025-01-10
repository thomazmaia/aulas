# Ex: um aluno tem cinco notas e deseja calcular a média aritmética dele. Crie um código para fazer ler as 5 notas do aluno e mostrar a média.
notas = [0, 0, 0, 0, 0]
# notas[0] = float(input("Digite a nota: "))
# notas[1] = float(input("Digite a nota: "))
# notas[2] = float(input("Digite a nota: "))
# notas[3] = float(input("Digite a nota: "))
# notas[4] = float(input("Digite a nota: "))

qtd_de_notas = len(notas)

soma = 0
for i in range(qtd_de_notas):
    notas[i] = float(input("Digite a nota: "))
    soma = soma + notas[i]

media  = soma/qtd_de_notas
print(f"Média = {media}")