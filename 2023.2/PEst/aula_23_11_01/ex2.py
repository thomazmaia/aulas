estoque = [
    ["camiseta", 5],  
    ["calça", 3], 
    ["sapato", 4]
    ]

def vender_produto(nome):
#    global estoque
    for item in estoque:
        if item[0] == nome:
            if (item[1] - 1) <= 0:
                estoque.remove(item)
            else:
                item[1] -= 1


print(f"Antes: {estoque}")
vender_produto("calça")
vender_produto("calça")
print(f"Depois: {estoque}")
vender_produto("calça")
print(f"Final: {estoque}")