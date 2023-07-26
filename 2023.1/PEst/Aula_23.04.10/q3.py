# 3. Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.

def eh_multiplo(val1, val2):
    if val1 % val2 == 0:
        return True
    else:
        return False
    
print( eh_multiplo(8, 4) )
print( eh_multiplo(7, 3) )
print( eh_multiplo(6, 2) )
