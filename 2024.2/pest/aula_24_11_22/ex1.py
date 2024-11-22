### TYPE ANNOTATIONS (TYPE HINT) - "dica"
# São uma forma de indicar o tipo de dados que um parâmetro pode receber.

# Ex: Crie uma função para receber um nome e escreva na tela "Olá nome".

def ola(nome : str):
    print(f"Olá {nome}")


ola(100)
ola(23.1)
ola(True)
ola("Maria")
ola("Joao")
ola("Qualquer coisa")