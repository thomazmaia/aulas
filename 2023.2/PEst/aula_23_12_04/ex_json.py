import json

dict_teste = dict()

while True:
    op = input("Digite s para sair.")
    if op in 'sS':
        break
    else:
        chave = input("Chave: ")
        valor = input("Valor: ")
        dict_teste[chave] = valor
    
with open("teste.json", "w") as f:
    json.dump(dict_teste, f)

print("Lendo o JSON...")

my_dict = {}
with open("teste.json", "r") as f:
    my_dict = json.load(f)

print(my_dict)
print(dict_teste)