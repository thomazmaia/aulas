# Escreva um programa em Python que resolve a versão geral do problema acima. Peça ao usuário que entre com a hora atual (em horas) e que entre com o número de horas que deverá esperar antes do alarme tocar. Seu programa deve imprimir a hora que o alarme irá tocar

hora_inicial = int(input("Digite a hora atual: "))
alarme = int(input("Digite daqui a quantas horas você quer que alarme: "))

hora_final = ((hora_inicial) + alarme) % 24

print(f"O alarme irá tocar às {hora_final}h")