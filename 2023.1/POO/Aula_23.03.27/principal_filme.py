from classe_filme import *

um_filme_qualquer = Filme("Os Vingadores", 142)
um_filme_qualquer.exibir_duracao_em_horas()

meu_filme_favorito = Filme("Men of honor", 100)
meu_filme_favorito.duracao_em_minutos = 129
meu_filme_favorito.exibir_duracao_em_horas()

print(f"Os filmes no catálogo são {um_filme_qualquer.titulo} e {meu_filme_favorito.titulo}.")