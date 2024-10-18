# 2. Escreva um código para classificar uma nota de 0 a 10 dada. Se a nota for maior ou igual a 9, imprima "A", se a nota for maior ou igual a 7 e menor que 9 imprima "B", se a nota for maior ou igual a 5 e menor que 7 imprima "C" e se a nota for menor que 5 imprima "D". Utilize uma única linha de código dentro de cada bloco 'if', 'elif' e 'else'.


nota = float(input("Digite uma nota: "))

if (nota >= 9):
    print("A")
elif ((nota >= 7) and (nota < 9)):
    print("B")
elif ((nota >= 5) and (nota < 7)):
    print("C")
elif (nota < 5):
    print("D")