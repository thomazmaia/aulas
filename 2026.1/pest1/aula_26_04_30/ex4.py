str1 = "Banana"
str2 = "Laranja"

aux = str1[0]
str1[0] = str2[0]
str2[0] = aux


print(str1)
print(str2)