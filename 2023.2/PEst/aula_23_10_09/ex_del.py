L = list()

L.append("a")
L.append("e")
L.append("i")
L.append("u")

print(L)

if "a" in L:
    L.remove("a")
if "e" in L:
    L.remove("e")
if "i" in L:
    L.remove("i")
if "o" in L:
    L.remove("o")
if "u" in L:
    L.remove("u")

# for item in L:
#     if item == "a":
#         L.remove(item)
#     if item == "e":
#         L.remove(item)
#     if item == "i":
#         L.remove(item)
#     if item == "o":
#         L.remove(item)
#     if item == "u":
#         L.remove(item)

print(L)
