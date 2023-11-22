x = float(input("x: "))
y = float(input("y: "))

if (-1 <= x and x <= 1) and (-1 <= y and y <= 1):
    print("A2")
elif (2 <= x and x <= 4) and (-2 <= y and y <= 1):
    print("A3'")
elif (-1 <= x and x <= 4) and (-4 <= y and y <= -2):
    print("A3''")
elif (-5 <= x and x <= -4) and (-3 <= y and y <= 1):
    print("A1'")
elif (-5 <= x and x <= -2) and (1 <= y and y <= 4):
    print("A1''")
elif (-2 <= x and x <= 3) and (3 <= y and y <= 4):
    print("A1'''")
else:
    print("Área inválida")