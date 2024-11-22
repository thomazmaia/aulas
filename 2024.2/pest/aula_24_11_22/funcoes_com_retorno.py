# Função sem retorno:
# print("Escreve alguma coisa")

# Função COM retorno:
# var = input("Vou ler algo: ")

# Crie uma função que receba dois parâmetros: a altura e a largura de um retângulo. Sua função deve calcular e RETORNAR a área desse retângulo.
# Teste a função.


def calc_area_retangulo(altura, largura):
    area = altura * largura
    return area
    

var = calc_area_retangulo(2, 5)
print(f"Área = {var}")