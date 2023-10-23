# Você está desenvolvendo um programa para um sistema de automação residencial
# que controla a iluminação em uma sala com base na luminosidade ambiente e na
# presença de pessoas. O sistema possui as seguintes regras:
# 1. Se a luminosidade for menor que 100 lux e não houver presença de pessoas,
# as luzes devem estar apagadas.
# 2. Se a luminosidade for menor que 100 lux e houver presença de pessoas,
# as luzes devem estar acesas.
# 3. Se a luminosidade estiver entre 100 e 500 lux (inclusive) e não houver
# presença de pessoas, as luzes devem estar em modo de economia de energia (meia-luz).
# 4. Se a luminosidade for maior que 500 lux, independentemente da presença de
# pessoas, as luzes devem estar acesas em plena intensidade

# Seu objetivo é escrever um programa em Python que, com base na luminosidade
# (um valor inteiro) e na presença de pessoas (um valor booleano True ou False),
# determine o estado das luzes na sala.

luminosidade = int(input("Luminosidade: "))
presenca = input("Pessoas no ambiente? <sim/nao> ")
if presenca == "sim":
    pessoas = True
else:
    pessoas = False

if luminosidade < 100 and pessoas == False:
    print("Luzes apagadas")
elif luminosidade < 100 and pessoas == True:
    print("Luzes acesas")
elif luminosidade > 100 and luminosidade <= 500 and pessoas == False:
    print("Economia de energia (meia-luz)")
elif luminosidade > 500:
    print("Luzes acesas em plena intensidade")
