# 1 - Introdução
#   'def' é a palavra-chave para definir uma função
#   'escreve_saudacao' é o NOME da função
#   parâmetros: vazio, nesse caso, mas são os parâmetros da função e vão dentro dos parênteses (obrigatórios)
#   corpo da função: é a função propriamente dita (o código!).

def escreve_saudacao():
    print("Olá muMdo!")
    print("Estou dentro da função")

print("Iniciando um programa!")
num = input("Digite um número: ")
escreve_saudacao()
print(f"O número que você escreveu foi {num}")

# 2. Parâmetros e argumentos
# Parâmetros são variáveis que são declaradas na definição de uma função. Eles são utilizados para RECEBER valores quando a função é chamada.
# Argumentos são os valores que são passados para DENTRO da função quando ela é chamada.
# Ex:
# def escreve_nome(nome):
#     print(f"Olá {nome}")
#
# escreve_nome("Maria")
# Nesse exemplo, "nome" é um parâmetro e "Maria" é um argumento.

# Uma função pode ter múltiplos parâmetros. Eles devem ser separados por vírgula.
# Ex:
# def escreve_nomes(nome1, nome2, nome3):
#    print("A equipe é formada por:")
#    print(nome1)
#    print(nome2)
#    print(nome3)

# escreve_nomes("Maria", "Julia", "Gabi")