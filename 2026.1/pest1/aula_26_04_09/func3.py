# Funções SEM retorno: são funções que executam uma tarefa, mas NÃO retornam um valor. Elas podem realizar ações como imprimir resultados, modificar variáveis globais ou interagir com o usuário, mas não fornecem um valor de saída que possa ser usado em outras partes do código.

# Funções COM retorno: são funções que executam uma tarefa e retornam um valor. Elas utilizam a palavra-chave "return" para enviar um resultado de volta ao local onde a função foi chamada. O valor retornado pode ser armazenado em uma variável, usado em expressões ou passado como argumento para outras funções.


def calcula_area(base, altura):
    area = base * altura
    return area

area1 = calcula_area(5, 2)
area2 = calcula_area(3, 2)

area_total = area1 + area2

print(area_total)