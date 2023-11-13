lista_de_tarefas = []
lista_de_tarefas_concluidas = []

def add_tarefa(tarefa):
    item = [tarefa, 'to-do']
    lista_de_tarefas.append(item)

def edit_tarefa(titulo_atual, titulo_novo):
    for item in lista_de_tarefas:
        if item[0] == titulo_atual:
            item[0] = titulo_novo

def list_tarefas(status):
    print(f"Tarefas {status}:")
    if status == 'done':
        for item in lista_de_tarefas_concluidas:
            print(f"- {item[0]}")
    else:       
        for item in lista_de_tarefas:
            if item[1] == status:
                print(f"- {item[0]}")

def iniciar_tarefa(titulo):
    print(f"Iniciando {titulo}")
    for item in lista_de_tarefas:
        if item[0] == titulo:
            item[1] = 'doing'

def concluir_tarefa(titulo):
    for item in lista_de_tarefas:
        if item[0] == titulo:
            item[1] = 'done'
            lista_de_tarefas_concluidas.append(item)
            lista_de_tarefas.remove(item)

def menu():
    print("LISTA DE TAREFAS\n[0] - SAIR\n[1] - Cadastrar tarefa\n[2] - Editar tarefa\n[3] - Iniciar tarefa\n[4] - Concluir tarefa\n[5] - Listar todas as tarefas\n[6] - Listar tarefas pendentes\n[7] - Listar tarefas em execução\n[8] - Listar tarefas concluídas")
    opcao = int(input("Opção: "))
    return opcao

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        titulo = input("Título da tarefa: ")
        add_tarefa(titulo)
    elif opcao == 2:
        titulo1 = input("Título da tarefa a EDITAR: ")
        titulo2 = input("Novo título: ")
        edit_tarefa(titulo1, titulo2)
    elif opcao == 3:
        titulo = input("Título da tarefa: ")
        iniciar_tarefa(titulo)
    elif opcao == 4:
        titulo = input("Título da tarefa: ")
        concluir_tarefa(titulo)
    elif opcao == 5:
        list_tarefas('to-do')
        list_tarefas('doing')
        list_tarefas('done')
    elif opcao == 6:
        list_tarefas('to-do')
    elif opcao == 7:
        list_tarefas('doing')
    elif opcao == 8:
        list_tarefas('done')