# 3. Suponha que você está desenvolvendo um app para registrar pedidos em um restaurante. Crie uma lista de pedidos, onde cada pedido é uma lista de itens do menu. Use extend() para adicionar novos pedidos e pop() para remover pedidos após serem entregues.

pedidos = [['Sanduba', 'Refri'], ['Milkshake']]
novos_pedidos = [["Salada", "Suco"], ["Batata Frita", "cerveja"]]

pedidos.extend(novos_pedidos)

print(pedidos)

x = pedidos.pop(1)
print(f"{x} foi retirado de {pedidos}")