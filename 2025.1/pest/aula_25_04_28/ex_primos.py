# Crie um código em Python que calcule a soma dos números primos de 1 a 100 (inclusive) usando o comando for.

def eh_primo(i : int):
    if i <= 1:
        return False
    if i == 2:
        return True
    if i % 2 == 0:
        return False
    for n in range(3, int(i ** 0.5) + 1, 2):
        if i % n == 0:
            return False
    return True


N = int(input("Digite um número: "))
if eh_primo(N) == True:
    print("Seu número é primo")
else:
    print("Não é primo")

# soma = 0

# for i in range(1, 101, 1):
#     if eh_primo(i) == True:
#         print(f"{i} é primo")
#         soma = soma + i # Só soma se 'i' for primo

# print(soma)