# PARÂMETROS POSICIONAIS
# São os parâmetros que são passados à função na ordem que são declarados via argumentos.

# PARÂMETROS NOMEADOS
# São os paâmetros que são passados à função pelo nome junto ao argumento.

def saudacao(nome : str, idade : int):
    print(f"Olá, {nome}! Você tem {idade} anos")

print("Parâmetros posicionais: ")
saudacao(30, "bob")            # Parâmetro posicional
saudacao("bob", 30)            # Parâmetro posicional
print("Parâmetros nomeados: ")
saudacao(idade=30, nome="bob") # Parâmetro nomeado
saudacao(nome="bob", idade=30) # Parâmetro nomeado

# PARÂMETROS COM VALORES PADRÃO
# São usados para definir um valor padrão para um parâmetro. Isso permite que o usuáro não seja obrigado a passar um valor para um parâmetro quando a função for chamada.

def saudar(nome : str = "Lorenzo", idade : int = 0):
    if idade == 0:
        print(f"Olá, {nome}! Bem vindo ao mundo!")
    else:
        print(f"Olá, {nome}! Você tem {idade} anos")

saudar("João", 30)
saudar(idade=15, nome="Maria")
saudar("Enzo")
saudar()