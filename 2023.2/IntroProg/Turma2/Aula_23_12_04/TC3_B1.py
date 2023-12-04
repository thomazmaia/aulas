
print("--- TABUADA ---")
print("1 - Tabuada de +")
print("2 - Tabuada de -")
print("3 - Tabuada de x")
print("4 - Tabuada de /")
op = int(input("Escolha uma opção: "))
N = int(input("Digite o número: "))

contador  = 1

if op == 1:
    while contador <= 10:
        res = contador + N
        print(f"{contador} + {N} = {res}")
        contador += 1    
elif op == 2:
    while contador <= 10:
        res = contador - N
        print(f"{contador} - {N} = {res}")
        contador += 1            
elif op == 3:
    while contador <= 10:
        res = contador * N
        print(f"{contador} x {N} = {res}")
        contador += 1
elif op == 4:
    while contador <= 10:
        res = contador / N
        print(f"{contador} / {N} = {res}")
        contador += 1    