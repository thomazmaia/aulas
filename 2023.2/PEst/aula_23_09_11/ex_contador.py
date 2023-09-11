def minha_funcao():
    global contador
    contador -= 1


contador = 0
while contador < 5:
    contador += 1
    print(f"Contador: {contador}")
    minha_funcao()
