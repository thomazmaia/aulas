# 8. Peça ao usuário para inserir uma série de números inteiros em uma lista. Em seguida, ordene a lista em ordem crescente usando o método insert para inserir cada número na posição correta. Por fim, imprima a lista ordenada.

lista = []

while True:
    elemento = int(input("Digite um número ou '-1' para sair: "))
    if elemento == -1:
        break
    else:
        if len(lista) == 0:
            lista.insert(0, elemento)
        elif len(lista) == 1:
            if elemento > lista[0]:
                lista.insert(1, elemento)
            else:
                lista.insert(0, elemento)
        else:
            if elemento <= lista[0]:
                lista.insert(0, elemento)
            elif elemento >= lista[-1]:
                lista.insert(len(lista), elemento) # inserir no último elemento
            else:
                copia = lista[:]
                for i in range(len(copia)-1):
                    if elemento >= copia[i] and elemento < copia[i+1]:
                        lista.insert(i+1, elemento)

print(lista)