notas = {
    "Joao Vitor" : [9.5, 7.5, 6.1],
    "Roberto" : [6.3, 8.1, 9.2],
    "Fernando" : [7.8, 8.1, 4]
}

print( notas["Roberto"] )

for nota in notas["Roberto"]:
    print(nota)

notas["Roberto"].append(10)

print(notas)