N = int(input("Quantidade de pessoas: "))

contador = 1
acumulador = 0
while contador <= N:
    idade = int(input(f"Idade {contador}: "))
    acumulador += idade
    contador += 1

media = acumulador/N
print(f"Média de idade: {media}")

if media >= 0 and media <= 25:
    print("Turma jovem")
elif media > 25 and media <= 60:
    print("Turma adulta")
elif media > 60:
    print("Turma idosa")