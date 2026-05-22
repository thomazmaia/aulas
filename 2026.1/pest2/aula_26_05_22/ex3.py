# Crie um programa para verificar se um aluno passou de média ou não. Seu programa deve fazer o seguinte:
# - Ler 5 notas de um aluno (usuário/input) e armazená-las em uma lista
# - Seu programa deve calcular a Média Parcial (MP) desse aluno (utilize uma função "calc_media" para calcular a média)
# - Caso a média seja superior a 6 informe que o aluno está aprovado. Caso a média seja inferior a 3 informe que o aluno está reprovado. Caso contrário, leia uma nova nota (Prova Final - PF) do usuário e calcule a média final:
# Média Final (MF) = (MP + PF)/2
# - Caso a média final seja inferior a 5, informe que o aluno está reprovado. Caso contrário, informe que o aluno está aprovado.

def ler_notas():
    lista_de_notas = [0, 0, 0, 0, 0]
    for i in range(5):
        lista_de_notas[i] = float(input(f"Digite a nota {i+1}: "))

    return lista_de_notas


def calc_media(L : list):
    acc = 0
    for item in L:
        acc += item
    return acc/len(L)


notas = ler_notas()
media_parcial = calc_media(notas)

print(notas)
print(f"A média é de {media_parcial}")

if media_parcial >= 6:
    print("e você foi APROVADO!")
elif media_parcial < 3:
    print("e você foi REPROVADO!")
else:
    print("e você está de recuperação.")
    PF = float(input("Digite a nota da Prova Final: "))
    
    media_final = (media_parcial + PF)/2
    print(f"A média final é de {media_final}")
    if media_final >= 5:
        print("Você foi APROVADO na prova final.")
    else:
        print("Você foi REPROVADO na prova final.")