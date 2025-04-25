# Crie uma função para converter valores de Celsius para Fahrenheit.

def converte_para_f(temp_em_c : float):
    valor_em_f = 1.8 * temp_em_c + 32
    return valor_em_f


temp = 25
print(f"{temp} C é igual a {converte_para_f(temp)} F")