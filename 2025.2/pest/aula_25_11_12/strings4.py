# MÉTODOS DE STRINGS
# Métodos de strings são funções que pertencem ao tipo string e podem ser usadas para manipular ou obter informações sobre strings.
# Aqui estão alguns exemplos de métodos de strings em Python:
# 1) lower() - transforma sua string para minúsculo
# 2) upper() - transforma sua string para maiúsculo
# 3) split() - divide a string em substrings mediante um separador e armazena em uma lista de substrings. Caso não tenha separador, ele dividirá pelo espaço.
# 4) join() - une uma LISTA de strings baseado em um "juntador"
# 5) capitalize() - deixa a primeira letra maiúscula e o resto todo minúsculo
# 6) replace() - substitui uma (sub)string por outra
# 7) find() - retorna a primeira ocorrência do que se está buscando ou retorna '-1' caso não exista
# 8) index() - semelhante ao finde, mas dá erro se não encontrar
# 9) count() - retorna a quantidade de vezes que uma (sub)string aparece na string.
# 10) islower() - retorna TRUE se o texto for todo minúsculo

texto = "isso aqui eh um EXEMPLO de texto!"

print(f"Original: '{texto}'")

lower = texto.lower()
print(f"lower(): '{lower}'")

upper = texto.upper()
print(f"upper(): '{upper}'")

split = texto.split()
print(f"split(): '{split}'")

join = '_'.join(split)
print(f"join(): '{join}'")

capitalize = texto.capitalize()
print(f"capitalize(): '{capitalize}'")

replace = texto.replace("eh", "é")
print(f"replace(): '{replace}'")

find = lower.find('x')
print(f"find(): '{find}'")

index = lower.index('x')
print(f"index(): '{index}'")

count = lower.count(' ex')
print(f"count(): '{count}'")

if texto.islower():
    print("O texto é LOWER")
else:
    print("O texto NÃO é LOWER")