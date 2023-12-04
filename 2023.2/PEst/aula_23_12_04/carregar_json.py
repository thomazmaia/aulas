import json

with open("nome_do_arquivo.json", "r") as f:
    dicionario = json.load(f)

print(dicionario)