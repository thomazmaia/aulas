# Escopo de variáveis - Locais e Globais
# O escopo de uma variável se refere à região do código onde a variável é acessível e pode ser usada.
#
# Escopo Local (variáveis locais)
# São aquelas declaradas dentro de uma função. São acessíveis apenas dentro da função e não existem fora dela.
def funcao(parm):
    var = 1 # var é uma variável local


# Escopo Global (variáveis globais)
# São aqeuals declaradas fora de qualquer função (ou bloco de código). São acessíveis de qualquer parte do código, incluindo funções.
# OBS: Para modificar uma variável global em uma função você precisa declará-la global na função

def my_func():
    global x
    x = x + 1
    print(x)

x = 20 # x é uma variável global
if x % 2 == 0:
    res = "par" # res NÃO É uma variável global

my_func()
print(x)