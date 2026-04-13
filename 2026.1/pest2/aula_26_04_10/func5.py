# Escopo de variáveis
# Escopo é o local (região) do código em que as variáveis estão localizadas e, por sua vez, podem ser acessadas e visualizadas.

# Escopo LOCAL
# Variávels de escopo LOCAL só podem ser acessadas dentro do escopo local: funções e blocos de códigos, por exemplo.

# Escopo GLOBAL
# Variáveis de escopo GLOBAL podem ser acessadas de qualquer região incluindo dentro das funções e blocos de códigos.
# OBS: Para manipular uma variável GLOBAL a partir de um escopo local (dentro da função) é necessário definir a variavel como "GLOBAL"
# ex: global var


def minha_funcao():
    global X
    X = 21
    X = X + 10
    print(X)


X = 21

print(X)
minha_funcao()
print(X)