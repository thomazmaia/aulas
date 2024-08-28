# 2. Imagine que você está criando um app de agendamento de eventos. Crie uma lista de eventos e seus horários correspondentes. Use extend() para adiconar eventos de uma data para outra.

eventos_dia1 = ["Reunião 10:00", "Almoço 12:00", "Aula 15:00"]
eventos_dia2 = ["Jantar 18:00", "Netflix 21:00"]

eventos_dia1.extend(eventos_dia2)

for evento in eventos_dia1:
    print(evento)