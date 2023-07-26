# 6. Leia uma palavra do usuário e uma letra. Depois, verifque se essa letra está na palavra ou não.
# OBS: a letra pode aparecer maiúscula ou minúscula.
# Ex: 'a' existe em 'ABACAXI'

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

if letra.lower() in palavra.lower():
    print(f"A letra '{letra}' aparece na palavra '{palavra}'.")
else:
    print(f"A letra '{letra}' não aparece na palavra '{palavra}'.")
