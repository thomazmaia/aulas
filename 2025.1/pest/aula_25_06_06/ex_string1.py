str1 = 'abacaxi'
str2 = 'MELANCIA'

print(str1[3]) # 2
print(str2[2:]) # LANCIA

print(f"Tamanho da string 1: {len(str1)} caracteres")
print(f"Tamanho da string 2: {len(str2)} caracteres")

# Percorrendo os elementos
print(f"Imprimindo os caracteres de {str1}:")
for i in range(len(str1)):
    print(str1[i])

print(f"Imprimindo os caracteres de {str2}:")
for caractere in str2:
    print(caractere)