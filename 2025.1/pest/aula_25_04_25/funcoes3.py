# 1. PARÂMETROS POSICIONAIS
# - Os parâmetros posicionais são aqueles que são passados para a função na mesma ordem em que foram definidos. Eles são obrigatórios e devem ser fornecidos na chamada da função.
def saudacao(nome : str, idade : int = 0):
    print(f"Olá, {nome}! Você tem {idade} anos.")

saudacao("João", 25) # "João" é o argumento passado para o parâmetro 'nome' e 25 é o argumento passado para o parâmetro 'idade'

# 2. PARÂMETROS NOMEADOS
# - Os parâmetros nomeados são aqueles que podem ser passados para a função usando o nome do parâmetro. Eles são opcionais e podem ser fornecidos em qualquer ordem.
saudacao("Maria", 30)
saudacao(idade=30, nome="Maria")

# 3. PARÂMETROS COM VALORES PADRÃO
# - Os parâmetros com valores padrão são aqueles que têm um valor padrão definido na função. Se você não fornecer um valor para esse parâmetro na chamada da função, o valor padrão será usado.
saudacao("Xico")
saudacao("Xico", 18)