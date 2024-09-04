livros = {
    "Livro 1" : {"Titulo" : "A arte da guerra", "Autor" : "Sun Tzu","Ano" : 500},
    "Livro 2" : {"Titulo" : "O senhor dos aneis", "Autor" : "Tokien", "Ano" : 1954}
}

# Como acessar uma chave no dicionário interno
print(livros["Livro 1"]["Titulo"])

# Como iterar em um dicionário interno
for livro, detalhes in livros.items():
    print(f"Título do {livro}: {detalhes["Titulo"]}")