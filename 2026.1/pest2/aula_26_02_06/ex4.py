num = 5

fat = 1

if num < 0:
    print("Número inválido")
else:
    while num >= 0:
        if num == 0:
            print(f"Fatorial: {fat}")
            num -= 1        
        else:
            fat *= num
            num -= 1