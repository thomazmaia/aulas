def fibo(n):
    a = 0
    b = 1
    contador = 0
    while contador < n:
        print(a)
        proximo = a + b
        a = b
        b = proximo
        contador += 1

fibo(9)