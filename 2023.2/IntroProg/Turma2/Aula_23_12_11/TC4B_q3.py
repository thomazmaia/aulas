N = int(input("Digite um número: "))

contador = 1

anterior = 0
atual = 1

while contador <= N:
    print(atual)
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    contador += 1