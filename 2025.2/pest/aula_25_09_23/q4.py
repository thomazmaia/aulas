# Defina uma função chamada eh_primo que aceita um número como parâmetro e retorna True se o número for primo e False caso contrário.

def eh_primo(num : int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



if eh_primo(10):
    print("10 é primo")
else:
    print("10 não é primo")

if eh_primo(7):
    print("7 é primo")
else:
    print("7 não é primo")

if eh_primo(137):
    print("137 é primo")
else:
    print("137 não é primo")