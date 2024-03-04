# 1. Crie uma função que receba o comprimento e a largura de um retângulo, calcule e escreva a área desse retângulo.

def calc_area(comprimento : float, largura : float):
    area = comprimento * largura
    print(f"A área é {area}")


comp = float(input("Comprimento: "))
larg = float(input("Largura: "))

calc_area(comprimento=comp, largura=larg)