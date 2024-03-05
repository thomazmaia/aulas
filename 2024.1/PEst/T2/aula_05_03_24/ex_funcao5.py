# Valores padrão

def saudacao(nome : str = "Anônimo", idade : int = 18):
    print(f"Olá {nome} de {idade} anos")


saudacao()
saudacao("Maria")
saudacao(idade=10)
saudacao("Maria", 50)
saudacao(40, "Maria")
saudacao(idade=40, nome="Maria")