def minha_funcao():
    #  Escopo local (a função enxerga tudo)
    nome = "Maria"
    print(nome)

# Escopo global (não se enxerga o que tem dentro das funções)
nome = "João"
minha_funcao()
print(nome)