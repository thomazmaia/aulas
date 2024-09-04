# Como criar dicionários aninhados
livros = {
    "livro 1" : {
        "Titulo" : "A arte da guerra",
        "Autor" : "Sun Tzu",
        "Ano" : 500
    },
    "livro 2" : {"Titulo" : "O senhor dos aneis", "Autor" : "Tokien","Ano" : 1954}
}

# Como acessar elementos do dicionário
print(livros['livro 1']['Autor'])


# Como iterar em dicionários aninhados
for livro, detalhes in livros.items():
    print(f"Título do {livro}: {detalhes['Titulo']}")