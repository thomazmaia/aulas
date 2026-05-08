# Passo a passo para fazer o método capitalize
# 1. deixa tudo para minusculo - lower()
# 2. pega o primeiro caractere - str[0]
# 2.5. coloca o primeiro caractere para maiusculo
# 3. pega o resto da string str[1:]
# 4. soma as duas coisas anteriores

def meu_capitalize(str : str):
    str = str.lower()
    char1 = str[0].upper()
    resto = str[1:]
    nova_str = char1 + resto
    return nova_str

print(meu_capitalize("Nem Todo Mundo Odeia O John"))
