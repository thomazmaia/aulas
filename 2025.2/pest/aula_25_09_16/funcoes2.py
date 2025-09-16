# PARÂMETROS
# São as variáveis que são declaradas na definição (def) de uma função. Eles são utilizados para receber valores quando a função é chamada. Os parâmetros servem como "espaços reservados" para os valores que serão passados para a função quando ela for chamada. A função pode receber vários parâmetros desde que sejam separados por virgula.
# Ao lados dos parâmetros normalmente é colocado o TIPO do parâmetro como dica (type hint ou type annotation).

def funcao_ola(p1 : int, p2 : float):
    print(f"Parâmetro 1: {p1}")
    print(f"Parâmetro 2: {p2}")

# ARGUMENTOS
# São os valores reais que são passados para a função quando ela é chamda. Os argumentos são fornecidos na chamada da função e preenchem os "espaços reservados" (parâmetros) declarados na definição da função.

funcao_ola(3, 19.1)