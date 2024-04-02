# 8. Escreva uma função chamada `intercalar_letras` que aceite duas strings como entrada e retorne uma nova string contendo as letras intercaladas das duas strings, ou seja, a primeira letra da primeira string, a primeira letra da segunda string, a segunda letra da primeira string e assim por diante.
# Ex: `intercalar_letras("Olá", "Mundo!")` deve retornar "OMluándo!”

def intercalar_letras(str1 : str, str2 : str):
    tam1 = len(str1)
    tam2 = len(str2)
    tam_menor = 0

    if tam1 <= tam2:
        tam_menor = tam1
    else:
        tam_menor = tam2

    str_res = ''
    for i in range(tam_menor):
        str_res = str_res + str1[i] + str2[i]
    
    if tam1 >= tam2:
        str_res = str_res + str1[tam_menor:]
    else:
        str_res = str_res + str2[tam_menor:]
    return str_res

print(intercalar_letras("Abacaxi", "Abacate"))