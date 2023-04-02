from classe_elevador import *

ele = Elevador(10, 8)

while True:
    print(20*'-')
    print("Elevador do sucesso")
    print("[1] - Subir")
    print("[2] - Descer")
    print("[3] - Entrar")
    print("[4] - Sair")
    op = input("Digite a opção: (s para sair)")
    if op == '1':
        ele.sobe()
    elif op == '2':
        ele.desce()
    elif op == '3':
        ele.entra()
    elif op == '4':
        ele.sai()
    elif op in 'sS':
        break
    
