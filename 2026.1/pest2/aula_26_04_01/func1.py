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

param = "João"

print(f"Antes da função: {param}")

def saudacao(param):
    print(f"Oi, {param}")

print(f"Depois da função: {param}")

aluno1 = "Gaspar"
aluno2 = "Caio"
aluno3 = "Davi"
aluno4 = "Filipe"

saudacao(aluno1)
saudacao(aluno2)
saudacao(aluno3)
saudacao(aluno4)

print(f"Depois de tudo: {param}")

