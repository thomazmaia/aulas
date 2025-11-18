# DICIONÁRIOS
# Enquanto listas são coleções ordenadas de objetos, dicionários são estruturas "desordenadas" (até o Python 3.?). Contudo, ao invés de indexação posicional nos dicionários os itens/elementos são armazenados e buscados por uma CHAVE. Uma CHAVE localiza um VALOR.

# Exemplo: dicionário EN -> PT-BR
# [CHAVE] -> [VALOR]
# CHAIR -> Cadeira
# APPLE -> Maçã

# Exemplo: dicionário PT-BR -> PT-BR
# [CHAVE] -> [VALOR]
# Cadeira -> Assento móvel normalmente de madeira...

# 1. Como criar dicionários em Python
dicio = dict() # dicionário vazio

dicio_en_pt = {
    "one" : "ONE em português quer dizer: um",
    "two" : "TWO em português quer dizer: dois",
    "um" : "one"
}
print(dicio_en_pt)

# 2. Como acessar itens/elementos
# Em dicionários não acessamos os itens/elementos pela posição (índice) mas sim pela CHAVE. 
#print(dicio_en_pt[0]) # Erro
print(dicio_en_pt["two"]) # Erro

# 3. Como adicionar itens/elementos a um dicionário
dicio_en_pt["four"] = "Esse é o número quatro"
print(dicio_en_pt["four"])
dicio_en_pt["five"] = "Esse é o número cinco"

dicio_en_pt["one"] = 1
print(dicio_en_pt)