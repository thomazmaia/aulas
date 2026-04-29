# Crie uma FUNÇÃO que receba uma STRING e retorne True se tiver a letra "a" nessa string ou False se não tiver.

def verificar_str(string : str):
    tamanho = len(string)
    for i in range(tamanho):
        if (string[i] == 'a') or (string[i] == 'A'):
            return True
    
    return False

minha_string = "Aberto"
if verificar_str(minha_string) == True:
    print(f"Tem letra 'A' na string {minha_string}")
else:
    print(f"Não tem letra 'A' na string {minha_string}")