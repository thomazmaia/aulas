# Para modificar uma variável de escopo global (fora da função) dentro de um escopo local (dentro da função) você deve DECLARAR essa variável como uma variável GLOBAL.

def minha_funcao():
    global contador
    contador = 999
    print(f"Escopo LOCAL: {contador}")


contador = 3

minha_funcao()
print(f"Escopo GLOBAL: {contador}")