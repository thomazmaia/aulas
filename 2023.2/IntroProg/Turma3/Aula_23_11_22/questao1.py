A = int(input("Lado A: "))
B = int(input("Lado B: "))
C = int(input("Lado C: "))

if (A+B>C) and (A+C>B) and (B+C>A):
    # É triângulo!
    if A == B and B == C:
        print("Triângulo equilátero")
    elif (A == B and B != C) or (A == C and C != B) or (B == C and C != A):
        print("Triângulo isóceles")
    elif (A != B and A != C and B != C):
        print("Triângulo escaleno")

else:
    print("Triângulo inválido")