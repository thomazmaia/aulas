def contar_vogais(str):
    str = str.lower()
    qtd_de_vogais = 0
    tamanho_da_str = len(str)
    vogais = "aeiouáéíúóàèìòùâêîôûãõ"
    for i in range(tamanho_da_str):
        if str[i] in vogais:
            qtd_de_vogais += 1
    return qtd_de_vogais

str = "Algumá coisa"
N = contar_vogais(str)

print(f"{str} tem {N} vogais")