livros = {
    "livro1": {"titulo": "A Arte da Guerra", "autor": "Sun Tzu", "ano": 500},
    "livro2": ["O senhor dos Anéis", "J.R.R. Tokien", 1954],
}


print(livros["livro1"]["titulo"])
print(livros["livro1"]["autor"])
print(livros["livro1"]["ano"])

print(livros["livro2"][0])
print(livros["livro2"][1])
print(livros["livro2"][2])
