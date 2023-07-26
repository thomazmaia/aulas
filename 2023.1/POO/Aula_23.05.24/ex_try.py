lista = []
for i in range(5):
    lista.append(input(": "))

try:
    for i in range(6):
        print(lista[i])
except IndexError:
    print("Foi longe demais.. por isso quebrou!")

numero1 = input("Digite um numero: ")
numero2 = input("Digite um numero diferente de zero: ")

try:
    res = float(num1) / float(num2)
    print(f"A divisao de {num1} por {num2} é {res}")
except ZeroDivisionError:
    print("deu ruim porque voce colocou zero")
except ValueError:
    print("deu ruim porque voce colocou algo não numérico")
except NameError:
    print("Deu ruim pq o nome da variável mudou")
except:
    print("deu ruim por algum outro motivo")
