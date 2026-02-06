num = int (input ("Digite um número inteiro: "))

if num < 0:
    print("Número inválido")
else:
    fat = 1
    while num >= 0:
        if num == 0:
            print (f"Fatorial: {fat}")
            num = num - 1
        else:
            fat = fat * num 
            num = num - 1

