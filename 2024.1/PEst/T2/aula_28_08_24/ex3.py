# 3. Suponha que você está desenvolvendo um app para registrar pedidos em um restaurante. Crie uma lista de pedidos, onde cada pedido é uma lista de itens do menu. Use extend() para adicionar novos pedidos e pop() para remover pedidos após serem entregues.

pedidos = [
    ['Sanduba', 'Batata frita'], 
    ['Sorvete', 'Bacon'], 
    ['Salada', 'Suco']
    ]

novos_pedidos = [
    ['Refri'], 
    ['Milkshake'], 
    ['Queijo', 'Vinho']
    ]

pedidos.extend(novos_pedidos)

item_removido = pedidos.pop(3)

print(item_removido)
print(pedidos)