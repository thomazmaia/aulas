# Crie um programa que ajude a decidir qual é a melhor refeição com base no horário
# do dia. Solicite ao usuário que insira a hora atual (em formato 24 horas) e, em
# seguida, sugira o tipo de refeição apropriado (café da manhã, almoço, jantar ou
# lanche).

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

if horas >= 4 and horas <= 10:
    print("Café da manhã")
elif horas >= 11 and horas <= 14:
    print("Almoço")
elif horas > 14 and horas <= 18:
    print("Lanche")
elif horas > 18 and horas < 24:
    print("Jantar")
