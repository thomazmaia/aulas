# Crie um dicionário para armazenar LIVROS. Cada chave do dicionário terá o seguinte padrão "livroX" onde X é um número:
# livro1 : {}
# livro2 : {}
# livro3 : {}
# Para cada item desse dicionário, cadastre as informações de um livro conforme exemplo:
# livros = {
#     "livro1" : {
#         "titulo" : "Alice blabla",
#         "autor" : "Alguem"
#     },
#     "livro2" : {
#         "titulo" : "Emilia",
#         "autor" : "Monteiro"
#     }
# }

# Peça as informações para o usuário e crie o dicionário em tempo real.

livros = {}

qtd = int(input("Quantos livros você quer adicionar? "))

for i in range(qtd):
    string = "livro" + str(i+1)
    livros[string] = {}
    livros[string]["titulo"] = input("Digite o título do livro: ")
    livros[string]["autor"] = input("Digite o autor do livro: ")

print(livros)