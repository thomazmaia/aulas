# Fatiamento (slicing) de string 
# ex: range(início, fim, passo)

str = "Hoje é um bom dia"

# Fatiamento simples
print(str[0])  # Primeiro elemento
print(str[1])  # Segundo elemento
print(str[-1]) # Último elemento
print(str[-2]) # Penúltimo elemento

str = "Hoje é um bom dia"
# Fatiamento com intervalo
print(str[0:4])   # "Hoje"
print(str[10:13]) # "bom"
print(str[14:17]) # "dia"
print(str[14:])   # "dia"
print(str[10:])   # "bom dia"
print(str[0:])    # "Hoje é um bom dia"
print(str[:])     # "Hoje é um bom dia"

# Fatiamento com passo
print(str[0::4])   # "H mma"
print(str[-1::-1]) # "aid mob mu é ejoH"