def calcula_idade(idade : int = 3, nome : str = "Pessoa"):
    aux = idade + 1
    print(f"{nome}, ano que vem você terá {aux} anos")

calcula_idade(nome="Maria", idade=20)
calcula_idade()