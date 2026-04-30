# Crie uma FUNÇÃO que receba uma STRING e retorne True se tiver a letra "a" nessa string ou False se não tiver.

def verifica_letra_a(string : str):
    tamanho = len(string)

    for i in range(tamanho):
        if (string[i] == 'a') or (string[i] == 'A'):
            return True
    
    return False

if verifica_letra_a("Álbert") == True:
    print("Tem letra A")
else:
    print("Não tem letra A")