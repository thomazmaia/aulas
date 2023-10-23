# Você está desenvolvendo um programa de controle de tráfego para uma cidade
# inteligente. O sistema deve determinar a cor do semáforo em um cruzamento com
# base em algumas condições complexas. Aqui estão as regras:
# 1. Se a hora atual estiver entre 6h e 9h da manhã, o semáforo deve exibir a cor verde.
# 2. Se a hora atual estiver entre 9h e 18h, o semáforo deve exibir a cor vermelha.
# 3. Se a hora atual estiver entre 18h e 20h, o semáforo deve exibir a cor verde intermitente.
# 4. Se a hora atual estiver entre 20h e 23h, o semáforo deve exibir a cor amarela.
# 5. Se a hora atual estiver entre 23h e 6h da manhã, o semáforo deve exibir a cor vermelha intermitente.
# Leia hora atual a partir do usuário.

hora_atual = int(input("Hora atual: "))

if hora_atual >= 6 and hora_atual < 9:
    print("Verde")
elif hora_atual >= 9 and hora_atual < 18:
    print("Vermelho")
elif hora_atual >= 18 and hora_atual < 20:
    print("Verde intermitente")
elif hora_atual >= 20 and hora_atual < 23:
    print("Amarela")
elif hora_atual >= 23 or hora_atual < 6:
    print("Vermelho intermitente")
