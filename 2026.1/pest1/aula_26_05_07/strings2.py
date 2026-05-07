# Acessando elementos de strings
str = "Abacaxi"

print(f"Primeira letra: {str[0]}")
print(f"Última letra: {str[len(str)-1]}")

# Primeira maneira:
for i in range(len(str)):
    print(f"{i} - {str[i]}")

print("---------")

# Segunda maneira
for caractere in str:
    print(caractere)