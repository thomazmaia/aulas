tarefas = []

def escreve_menu():
    print('---------------------')
    print('LISTA DE TAREFAS')
    print('---------------------')
    print('[0] - Sair')    
    print('[1] - Adicionar tarefa')
    print('[2] - Remover tarefa')
    print('[3] - Listar tarefas')
    print('---------------------')
    opcao = int(input("Digite a opção: "))
    while opcao < 0 or opcao > 3:
        if opcao == 0:
            break
        print('Opção inválida!!')
        opcao = int(input("Digite a opção: "))
    return opcao

def add_tarefa(tarefa):
    tarefas.append(tarefa)

def rem_tarefa(tarefa):
    if tarefa not in tarefas:
        print("Essa tarefa não está na lista!")
    else:
        tarefas.remove(tarefa)

def listar_tarefas():
    print('---------------------')
    print('Tarefas: ')
    for item in tarefas:
        print(f"- {item}")
    print('---------------------')



while True:
    opcao = escreve_menu()
    if opcao == 0:
        break 
    elif opcao == 1:
        tarefa = input("Digite a tarefa: ")
        add_tarefa(tarefa)
    elif opcao == 2:
        tarefa = input("Digite a tarefa: ")
        rem_tarefa(tarefa)
    elif opcao == 3:
        listar_tarefas()