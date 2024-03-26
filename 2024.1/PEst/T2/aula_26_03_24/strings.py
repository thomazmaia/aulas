str = "Thomaz"

# Acessando os elementos:
print(f"Primeiro elemento:      {str[0]}") 
print(f"Segundo elemento:       {str[1]}")
print(f"Terceiro elemento:      {str[2]}") 
print(f"Último elemento:        {str[-1]}") 
print(f"Penúltimo elemento:     {str[-2]}") 
print(f"Antepenúltimo elemento: {str[-3]}") 

# Tamanho da string:
print(f"Tamanho da string: {len(str)}")

# Acessar todos os elementos da string
print("Acessando todos os elementos:")
for i in range(len(str)):
    print(str[i])
print("Acessando todos os elementos de trás para frente:")
for i in range(-1, -len(str)-1,  -1):
    print(str[i])
print("Acessando todos os elementos de trás para frente (v2):")
for i in range(len(str)-1, -1, -1):
    print(str[i])

print("Acessando todos os elementos (v2):")
for caractere in str:
    print(caractere)

