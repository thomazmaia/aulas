# PARÂMETROS E ARGUMENTOS DE FUNÇÕES
# - Parâmetros são variáveis que aparecem na definição da função e que recebem valores quando a função é chamada. Esses valores são chamados de argumentos.
# - Argumentos são os valores reais que você passa para a função quando a chama. Eles podem ser literais, variáveis ou expressões.
# ----------------------------------
# TYPE HINTS / ANNOTATIONS
# - Type hints (anotações de tipo) são uma maneira de indicar o tipo esperado dos parâmetros.

def calc_area_retangulo(base : float , altura : float):
    area = base * altura
    print(f"Área = {area}")


calc_area_retangulo(2, 3)
calc_area_retangulo(4, 5)
calc_area_retangulo(6, 7)
calc_area_retangulo(8, 9)