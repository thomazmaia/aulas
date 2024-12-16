def reverter(string : str):
    string_invertida = ''

    for i in range(-1, -len(string)-1, -1):
        print(f"Índice: {i} :: {string[i]}")
        string_invertida = string_invertida + string[i]
    
    return string_invertida



print(reverter("Abacaxi"))