nota_final = float(input("Digite sua nota final: "))

if nota_final >= 60:
    print("Aprovado")
elif nota_final >= 40 and nota_final < 60:
    print("Recuperação")
elif nota_final < 40:
    print("Reprovado")
