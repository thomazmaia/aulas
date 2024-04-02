# 7. Crie uma função chamada `invertendo_substrings` que receba duas strings como entrada e retorne uma nova string que consiste na primeira metade da segunda string invertida concatenada com a segunda metade da primeira string também invertida. Veja o exemplo abaixo.
# Ex: 'invertendo_substrings("Python", "Programming")'  deve retornar "gnimmtyP"

def invertendo_substrings(str1 : str, str2 : str):
    str2_invertida = str2[-1::-1]
    tam2 = len(str2_invertida)
    tam2_metade = tam2 // 2
    str2_res = str2_invertida[0:tam2_metade]
    
    str1_invertida = str1[-1::-1]
    tam1 = len(str1_invertida)
    tam1_metade = tam1 // 2
    str1_res = str1_invertida[-tam1_metade::]

    res = str2_res + str1_res
    return res


print(invertendo_substrings("Rayana", "Denylson"))