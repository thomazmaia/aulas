# Existem DUAS possíveis operações com strings:
# 1) "somar" é concatenar strings.
#    ex: str = 'olá' + ' ' + 'mundo' + '10'
#        print(str)
#
# 2) "multiplicar" é repetir strings
#    ex: str = "olê " * 4
#        print(str)

str = 'hoje é um bom dia'

inicio = str[0:10]
print(inicio)

fim = str[13: ]
print(fim)

nova_str = inicio + "mal" + fim
print(nova_str)