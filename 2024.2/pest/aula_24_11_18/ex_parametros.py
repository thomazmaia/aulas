# Crie uma função para receber um nome e imprimir esse nome.

def imprime_nome(nome):
    # Escopo local (dentro da função)
    print(f"Olá {nome}")


# Escopo global (fora da função)
imprime_nome("Maria")
imprime_nome("João")
imprime_nome("Francisco")