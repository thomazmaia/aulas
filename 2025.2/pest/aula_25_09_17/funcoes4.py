# FUNÇÕES COM RETORNO
# As funções podem ter retorno ou não. O retorno é um valor que a função "devolve" ao programa principal.

def pega_idade(nome : str):
    print(f"Olá {nome}")
    idade = int(input("Digite a sua idade: "))
    return idade


idade_joao = pega_idade("João")
idade_maria = pega_idade("Maria")

soma = idade_joao + idade_maria

print(f"A soma das idades dessa turma é {soma} anos")