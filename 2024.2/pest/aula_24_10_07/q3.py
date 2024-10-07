# Você olha para um relógio e são exatamente 2 da tarde. Você coloca um alarme para tocar daqui a 51 horas. A que horas o alarme irá tocar?
# OBS: desconsidere minutos e segundos

hora_inicial = 14
alarme = 51

hora_final = ((hora_inicial) + alarme) % 24

print(f"O alarme irá tocar às {hora_final}h")