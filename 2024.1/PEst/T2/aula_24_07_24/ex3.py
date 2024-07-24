def eh_palindromo(minha_str : str):
    minha_str = minha_str.lower()
    minha_str = minha_str.replace(" ", "")
    minha_str = minha_str.replace("á", "a")
    str_invertida = minha_str[::-1]

    if minha_str == str_invertida:
        return True
    else:
        return False

minha_string = "Anotaram a data da maratona"

if eh_palindromo(minha_string):
    print(f"{minha_string} é palindromo")
else:
    print(f"{minha_string} NÃO É palindromo")