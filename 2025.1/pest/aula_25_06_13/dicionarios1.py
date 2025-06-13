# DICIONÁRIOS - INTRODUÇÃO
# Dicionários são estruturas de dados que armazenam pares de chave-valor.
# Eles são mutáveis e não ordenados, permitindo acesso rápido aos valores através de suas chaves.
# Exemplo de dicionário


dicionario = {
    "one" : "um",
    "two" : "dois",
    "three" : "três"
}
#--------------------------------------
# COMO ACESSAR VALORES DE DICIONÁRIOS
# Não existe índice! Uma vez que NÃO SÃO estruturas ordenadas. As chaves são utilizadas para consulta de valores.
# print(dicionario['two']) # "dois"
# print(dicionario['one']) # "um"
# print(dicionario['four']) # KeyError
#--------------------------------------
# COMO ALTERAR UM VALOR
# Utilizamos a chave do item para alterar o valor
dicionario["two"] = 2
# print(dicionario['two']) # 2
#--------------------------------------
# Utilizamos uma nova chave para criar um novo valor
dicionario["four"] = "Esse é o número quatro"
print(dicionario)