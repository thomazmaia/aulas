from classes_questao3 import *

luan = Pessoa("Luan", "18/03/2005", "123.456.789-00")
luan.exibir_informacoes()
luan.calcular_idade()

agenda = Agenda()
agenda.armazenar_pessoa("Luan", "18/03/2005", "123.456.789-00")
agenda.armazenar_pessoa("Emilly", "12/01/2006", "123.456.789-00")
agenda.armazenar_pessoa("Thomaz", "08/03/1998", "123.456.789-00")
agenda.imprimir_agenda()
agenda.buscar_pessoa("Thomaz")
agenda.remover_pessoa("Luan")
agenda.imprimir_agenda()
agenda.imprimir_pessoa(1)
