# Desenvolva uma função chamada eh_positivo que receba um número inteiro como parâmetro e retorne True se o número for positivo ou False caso contrário. No programa principal, solicite um número ao usuário e exiba o resultado.

def eh_positivo(num : int):
    if num > 0:
        return True
    else:
        return False
    
numero = int(input("Digite um numero: "))
print(eh_positivo(numero))