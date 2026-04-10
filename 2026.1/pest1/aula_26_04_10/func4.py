# Type Annotations (type hint)
# Type annotations são uma forma de indicar o tipo de dados esperado para variáveis, parâmetros de funções e valores de retorno. Elas não afetam a execução do código, mas ajudam a melhorar a legibilidade e a manutenção do código, além de permitir que ferramentas de análise estática detectem possíveis erros de tipo.

# def xpto(A : int, B : str, C : bool) -> str: 
#     pass
#
# A função "xpto" recebe três parâmetros sendo "A" do tipo int, "B"do tipo str e "C" do tipo bool. A função retorna uma str.
def calcula_area(base : float, altura : float) -> float:
    area = base * altura
    return area


# Funções com parâmetros nomeados
# Atualmente trabalhamos com funções que possuem parâmetros posicionais, ou seja, a ordem dos argumentos é importante. Com parâmetros nomeados, podemos especificar os argumentos usando seus nomes, o que torna o código mais legível e flexível.
def calcula_idade(nome : str, idade : int):
    nova_idade = idade + 1
    print(f"{nome}, ano que vem você terá {nova_idade} anos")

calcula_idade(nome="Alguém", idade=20)

# Parâmetros com valores padrão
# Podemos definir valores padrão para os parâmetros de uma função. Isso significa que, se um argumento não for fornecido ao chamar a função, o valor padrão será usado. Isso torna a função mais flexível e fácil de usar.

def saudacao(nome : str = "Aluno", idade : int = 0):
    print(f"Bom dia {nome}. Ano que vem você terá {idade + 1} a")

saudacao(idade=10)