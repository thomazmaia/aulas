def eh_positivo(numero : float):
    if numero > 0:
        return "Positivo"
    else:
        return "Negativo"

N = float(input("Número: "))

X = eh_positivo(N)

print(f"O número {N} é {X}")

# if eh_positivo(N) == "Positivo":
#     print(f"O número {N} é positivo")
# else:
#     print(f"O número {N} é negativo")