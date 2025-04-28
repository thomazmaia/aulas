# Escopo de Funções
# - Variáveis definidas dentro de uma função só existem dentro dela
# - Variáveis definidas fora de uma função existem em todo o programa
# - Variáveis definidas dentro de uma função não podem ser acessadas fora dela
# - Variáveis definidas fora de uma função podem ser acessadas dentro dela


aux = "Estou vivo"

def minha_funcao():
    var = "Eu sou uma variável"
    print(var)
    global aux
    aux = "Eu estou BEM vivo"
    print(aux)

minha_funcao()
print(aux)