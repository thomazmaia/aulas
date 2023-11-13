x = float(input("X: "))
y = float(input("Y: "))

if (x >= 4 and x <= 5) and (y >= 4 and y <= 5):
    print("A2")
elif (x >= 1 and x <= 3) and (y >= 3 and y <= 5):
    print("A1")
elif (x >= 1 and x <= 5) and (y >= 2 and y <= 3):
    print("A1")
else:
    print("Área inválida")