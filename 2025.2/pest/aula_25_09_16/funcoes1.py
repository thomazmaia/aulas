# Material de apoio:
# Livro PENSE PYTHON (https://penseallen.github.io/PensePython2e/)
# Caps. 3 e 6
# --------------------
# Funções são blocos de códigos reutilizáveis. Elas são criadas para executar uma tarefa específica. Normalmente são utilizadas para organizar e modularizar o código.
# Sintaxe:
# def nome_da_funcao(parametros : tipo):
#     corpo da função

def diz_ola_mundo(): # Função sem parâmetros
    print("Olá Mundo!")


def diz_ola_alguem(nome : str): # Função com um parâmetro
    print(f"Olá, {nome}")


print("Aqui é o código principal.")
print("Aqui é executado pimeiro")
print("Agora vou chamar a função:")
diz_ola_mundo()
print("Agora voltei para o meu programa principal!")
diz_ola_alguem("Xikin") # "xikin" é um ARGUMENTO da função
diz_ola_alguem("Maria") # "Maria" é um ARGUMENTO da função
diz_ola_alguem("Joao") # "Joao" é um ARGUMENTO da função
diz_ola_alguem("Francisco") # "Francisco" é um ARGUMENTO da função
