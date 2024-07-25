def contar_vogais(string : str):
    string = string.lower()
    vogais = "aeiouáéíóúàèìòùãõ"
    qtd_de_vogais = 0
    for i in string:
        if i in vogais:
            qtd_de_vogais += 1
    return qtd_de_vogais


minha_string = "Olá, mundo"
N = contar_vogais(minha_string)

print(f"'{minha_string}' tem {N} vogais")