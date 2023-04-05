def soma(a, b):
    '''
    Essa função soma dois números 
    e mostra uma mensagem.
    'contador' é uma variável global.
    ex: soma(3, 5)
    saída: [contador] A soma de 3 + 5 é 8
    '''
    global contador
    contador += 1
    res = a + b
    print(f"[{contador}] A soma de {a} + {b} é {res}")

contador = 1
soma(3, 5)
soma(10, 5)
soma(2, 9)
print(soma.__doc__)