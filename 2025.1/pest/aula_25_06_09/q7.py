# ("Python", "Programming") -> "gnimmtyP"

# 1) Pega a 2a string e inverte ela: "gnimmargorP"
# 2) Pega a primeira metade dessa string invertida: "gnimm"
# 3) Pega a 1a string e inverte ela: "nohtyP"
# 4) Pega a 2a metade dessa string invertida: "tyP"
# 5) Concatena as strings dos passos 2 e 4: "gnimm" + "tyP"

def invertendo_substrings(s1 : str, s2: str):
    # Passo 1:
    s2_invertido = s2[::-1]
    # Passo 2:
    metade = int(len(s2_invertido)/2)
    substring1 = s2_invertido[0:metade]

    # Passo 3:
    s1_invertido = s1[::-1]
    # Passo 4:
    metade = int(len(s1_invertido)/2)
    substring2 = s1_invertido[metade:]

    # Passo 5:
    nova_string = substring1 + substring2
    return nova_string

print(invertendo_substrings("Abacaxi", "Melancia"))