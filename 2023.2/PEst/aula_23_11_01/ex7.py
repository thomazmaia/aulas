lista_de_eventos = []
eventos_em_outra_data = []

def add_evento(lista, evento, horario):
    compromisso = [evento, horario]
    lista.append(compromisso)


add_evento(eventos_em_outra_data,"Acordar", 5)
add_evento(eventos_em_outra_data,"IFCE", 6)
add_evento(lista_de_eventos,"Jantar", 19)
add_evento(lista_de_eventos,"Cinema", 16)
print("ANTES:")
print(lista_de_eventos)
print(eventos_em_outra_data)

lista_de_eventos.extend(eventos_em_outra_data)
print("DEPOIS:")
print(lista_de_eventos)
print(eventos_em_outra_data)

lista_de_eventos.pop()
print("DEPOIS:")
print(lista_de_eventos)
print(eventos_em_outra_data)