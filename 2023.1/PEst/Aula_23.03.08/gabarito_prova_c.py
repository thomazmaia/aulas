def q1():
    idade = 55
    if idade < 18:
        resultado = "Menor de idade"
    elif idade >= 18 and idade < 50:
        resultado = "Adulto"
    else:
        resultado = "Idoso"
        if idade > 60:
            resultado = resultado + " (acima de 90 anos)"
        else:
            resultado = resultado + " (entre 50 e 60 anos)"
    print(resultado)

def q2():
    soma = 0
    i = 0
    while i < 9:
        i += 1
        if i % 2 == 0:
            soma = soma + i
        elif i % 3 == 0:
            soma = soma - i
        else:
            soma = soma * i
    print (soma)

def q3():
    num = 0
    while num < 10:
        num += 1
        if num % 2 == 0:
            break
        elif num == 7:
            continue
        else:
            print(num)
    print("Fim do programa")

def q4():
    for i in range (1, 6):
        if i % 2 == 0:
            print(i * 3)
        else:
            print(i * 2)

def q5():
    soma = 0
    for i in range(1, 10):
        j = i
        while j > 0:
            if j % 2 == 0:
                soma = j + 1
                break
            else:
                j = j - 1
                continue
    print(soma)


print("PROVA B")
print(20*"-")
print(f"{'QUESTÃO 1': ^20}")
print(20*"-")
q1()
print(20*"-")
print(f"{'QUESTÃO 2': ^20}")
print(20*"-")
q2()
print(20*"-")
print(f"{'QUESTÃO 3': ^20}")
print(20*"-")
q3()
print(20*"-")
print(f"{'QUESTÃO 4': ^20}")
print(20*"-")
q4()
print(20*"-")
print(f"{'QUESTÃO 5': ^20}")
print(20*"-")
q5()