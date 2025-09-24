# ESCOPO DE VARIÁVEIS
# É, basicamente, o local onde aquela variáveis existirão.
# ESCOPO LOCAL: dentro das funções
# ESCOPO GLBOAL: fora das funções (dentro do programa principal)
# De modo geral, as variáveis não se conversam entre escopos diferentes

var = "oi"

def funcao():
    var = "tchau"
    print(var)

print(var)
var = "olá"
funcao()
print(var)