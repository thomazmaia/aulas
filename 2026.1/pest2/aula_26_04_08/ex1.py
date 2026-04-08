def calcular_area(base, altura):
    area = base * altura
    return area

A1 = calcular_area(1.5, 4.7)
A2 = calcular_area(5, 1)
A3 = calcular_area(1, 3)
A4 = calcular_area(2, 2)

area_final = A1 + A2 + A3 + A4
print(f"Área final = {area_final}")