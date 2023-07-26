                    # Argumentos padrão:
def dar_boas_vindas(nome="Usuario", local="IFCE"):
    print(f"Oi {nome}")    
    print(f"Seja bem vindo ao {local}")
    print("É muito bom tê-lo aqui conosco.")

# Argumentos posicionais
dar_boas_vindas("Thomaz", "Maranguape")
# Argumentos nomeados (não importa a posição)
dar_boas_vindas(local="Colégio", nome="Artur")
# Argumentos padrão
dar_boas_vindas()