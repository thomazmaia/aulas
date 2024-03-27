# Operações entre strings

# 1. Concatenação ("soma") de strings
str1 = "Bom"
str2 = " "
str3 = "Dia"
res = str1 + str2 + str3
print(res)

# 2. Repetição ("multiplicação") de strings
str1 = "Olê "
res = 4 * str1 + "Olá"
print(res)

# Leia uma string do usuário e substitua o primeiro caractere por um asterisco "*".
# Ex: string = "Bom dia" deve virar "*om dia"
str = "Bom dia"
str2 = "*" + str[1:]

print(str2)