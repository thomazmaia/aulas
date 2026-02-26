N = int(input(""))

u = N % 10
d = (N // 10) % 10
c = ((N // 10) // 10) % 10
m = (((N // 10) // 10) // 10) % 10

print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")

if u != d and d != c and c != m and u != c and u != m:
    print("Os dígitos são diferentes entre si")
else:
    print("Existem dígitos iguais")