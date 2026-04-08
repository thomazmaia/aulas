# Funções SEM retorno:
# são funções que realizam uma tarefa específica, mas não retornam um valor de saída. Elas podem modificar variáveis globais ou imprimir resultados na tela, mas não podem ser usadas em expressões ou atribuídas a variáveis.
# Ex: função para calcular a área de um retângulo, função para calcular a idade de uma pessoa no próximo ano, função para imprimir uma saudação personalizada, etc.
def saudacao(param):
    print(f"Oi, {param}")

saudacao("João")
saudacao("Maria")

# Funções COM retorno:
# são funções que realizam uma tarefa específica e retornam um valor de saída. Elas podem ser usadas em expressões ou atribuídas a variáveis, e podem ser chamadas várias vezes em um programa.
# Ex: função para calcular a área de um retângulo, função para calcular a idade de uma pessoa no próximo ano, função para calcular a média de uma lista de números, etc.
def calcular_area(base, altura):
    area = base * altura
    return area

A1 = calcular_area(5, 8)
A2 = calcular_area(20, 7)
area_final = A1 + A2
print(f"Área final = {area_final}")
