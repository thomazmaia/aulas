# 10. Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o número mínimo e o número máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores máximo e mínimo e, falso, caso contrário

def verifica_string(palavra, val_min, val_max):
    tamanho = len(palavra)
    if tamanho >= val_min and tamanho <= val_max:
        return True
    else:
        return False
    
print( verifica_string("Abacaxi", 1, 10) )
print( verifica_string("será que funciona?", 1, 10) )