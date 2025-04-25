# FUNÇÕES COM RETORNO
# Funções podem retornar valores usando a palavra-chave return. Isso permite que você obtenha resultados de uma função e os utilize em outras partes do seu código.

def calc_area_retangulo(base : float , altura : float):
    area = base * altura
    return area


res = calc_area_retangulo(3, 5)
print(f"O valor de área retornado foi {res}")