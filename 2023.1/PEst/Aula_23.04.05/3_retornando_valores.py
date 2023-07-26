def calcula_imc(peso, altura):
    imc = peso/(altura*altura)
    return imc
def verifica_condicao(imc):
    if imc < 18.5:
        print(f"Seu imc é {imc} e você está com BAIXO PESO")
    elif imc >= 18.5 and imc < 24.99:
        print(f"Seu imc é {imc} e você está NORMAL")
    elif imc >= 25 and imc < 29.99:
        print(f"Seu imc é {imc} e você está com SOBREPESO")
    elif imc >= 30:
        print(f"Seu imc é {imc} e você está OBESO")

def calcula_e_verifica_imc(peso, altura):
    verifica_condicao(calcula_imc(peso, altura))

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
calcula_e_verifica_imc(peso, altura)





#imc = calcula_imc(peso, altura)
#verifica_condicao(imc)