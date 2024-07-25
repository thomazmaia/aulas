def eh_palindromo(string : str):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace("á", "a")
    string_invertida = string[::-1]
    if string_invertida == string:
        return True
    else:
        return False


minha_string = "Ánotaram a data da maratona"

if eh_palindromo(minha_string):
    print(f"'{minha_string}' é palindromo")
else:
    print(f"'{minha_string}' NÃO É palindromo")