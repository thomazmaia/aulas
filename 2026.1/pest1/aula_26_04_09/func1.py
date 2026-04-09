# Funções: funções são blocos de código que realizam uma tarefa específica. Elas podem receber parâmetros de entrada e retornar um valor de saída.

# Características de uma função:
# 1. Reutilizável: uma função pode ser chamada várias vezes em um programa
# 2. Modular: uma função pode ser usada para dividir um programa em partes menores e mais gerenciáveis
# 3. Abstrata: uma função pode ser usada para ocultar detalhes de implementação

# Sintaxe das funções:
# def nome_da_funcao(parametros):
#   corpo da função
#
#  - def :: é a palavra-chave usada para definir uma função
#  - nome_da_funcao :: é o nome da função e obedece as mesmas regras dos nomes das variáveis
#  -  parametros:: são valores externos necessários à execução da função. Parâmetros são OPCIONAIS (vai depender do objetivo da função)
#  - corpo da função :: é o código que será executado quando a função for chamada

def saudacao(nome):
    print(f"Bom dia, {nome}")

nome = "John"
saudacao("José")
print(f"Boa tarde, {nome}")
saudacao("Maria")