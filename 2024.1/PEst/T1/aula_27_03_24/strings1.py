str = "ALO ALO   ALO"

# Acessando elementos
print(f"Primeiro elemento:       {str[0]}")
print(f"Segundo elemento:        {str[1]}")
print(f"Terceiro elemento:       {str[2]}")
print(f"Último elemento:         {str[-1]}")
print(f"Penúltimo elemento:      {str[-2]}")
print(f"Antepenúltimo elemento:  {str[-3]}")

# Tamanho da string
tamanho = len(str)
print(f"Tamanho da string: {tamanho} caracteres")

# Acessar todos os elementos da string
print("Acessando todos os elementos da string:")
for i in range(tamanho):
    print(str[i])

print("Acessando todos os elementos de trás para frente:")
for i in range(tamanho-1, -1, -1):
    print(str[i])

print("Acessando todos os elementos de trás para frente (v2):")
for i in range(-1, -tamanho-1, -1):
    print(str[i])

print("Acessando todos os elementos da string (v2):")
for caractere in str:
    print(caractere)