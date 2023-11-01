temperaturas = []

def listar_temperaturas():
    for item in temperaturas:
        print(item)

def add_temperatura(dia, temp):
    novo_registro = [dia, temp]
    temperaturas.append(novo_registro)

def limpar_fds():
    for item in temperaturas:
        if item[0] == 'sab' or item[0] == 'dom':
            item.clear()

add_temperatura("seg", [1, 2, 3, 4])
add_temperatura("ter", [1, 2])
add_temperatura("qua", [6, 7])
add_temperatura("qui", [1, 2, 7, 5])
add_temperatura("sex", [5, 6, 7])
add_temperatura("sab", [0, 1, 2])
add_temperatura("dom", [6, 5, 2])

print("ANTES:")
listar_temperaturas()

limpar_fds()
print("DEPOIS:")
listar_temperaturas()