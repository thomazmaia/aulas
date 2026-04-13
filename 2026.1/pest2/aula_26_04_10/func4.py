# Type Annotations (type hint)
# Type annotations são uma forma de indicar o tipo de dados esperado para variáveis, parâmetros de funções e valores de retorno. Elas não afetam a execução do código, mas ajudam a melhorar a legibilidade e a manutenção do código, além de permitir que ferramentas de análise estática detectem possíveis erros de tipo.

def xpto(A : str, B : int, C : float) -> int:
    return 0

xpto(10, 10, 10)


# Funções com parâmetros nomeados
# Atualmente trabalhamos com funções que possuem parâmetros posicionais, ou seja, a ordem dos argumentos é importante. Com parâmetros nomeados, podemos especificar os argumentos usando seus nomes, o que torna o código mais legível e flexível.

def calcula_idade(nome : str, idade : int):
    aux = idade + 1
    print(f"{nome}, ano que vem você terá {aux} anos")

calcula_idade(idade=20, nome="maria")
calcula_idade(nome="maria", idade=20)




# Parâmetros com valores padrão
# Podemos definir valores padrão para os parâmetros de uma função. Isso significa que, se um argumento não for fornecido ao chamar a função, o valor padrão será usado. Isso torna a função mais flexível e fácil de usar.
# OBS: Parâmetros com valores padrão devem vir por último na definição da função

def saudacao(param : str = "pessoa"):
    print(f"Olá, {param}")


saudacao("Agatha")
saudacao("")
saudacao()