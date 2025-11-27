# Dicionários aninhados (dicionário dentro de dicionário)

pessoas = {
    "renan" : {
                "idade" : 18,
                "bairro" : "santos dumont"
            },
    "thainara" : {
                "idade" : 17,
                "bairro" : "novo maranguape 1"
            },
    "tamires" : {
                "idade" : 19,
                "bairro" : "centro"
            },
    "carla" : {
                "idade" : 16,
                "bairro" : "novo maranguape 1"
            },
    "cristhian" : {"idade" : 18,"bairro" : "novo pq iracema"},
    "felipe" :  {"idade" : 17,"bairro" : "itapebussu"}
}

nome = input("Digite o nome da pessoa: ")
oque = input(f"Digite o que você quer saber do/da {nome}: ")

if nome in pessoas:
    print(pessoas[nome][oque])
else:
    print(f"{nome} não cadastrado")