# Crie uma função chamada media_lista que aceita uma lista de números numeros como
# parâmetro e retorna a média dos números na lista.


def media_lista(numeros):
    tamanho_da_lista = len(numeros)
    soma = 0
    for item in numeros:
        soma += item
    media = soma / tamanho_da_lista
    return media


L = [2, 4, 10, 4]
media = media_lista(L)
print(f"Média da lista: {media}")
