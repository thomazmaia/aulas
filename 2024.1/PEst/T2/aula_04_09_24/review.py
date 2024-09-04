dicionario = {
    'computador' : 40,
    'datashow' : 1,
    'teclado' : 40,
    'mouse' : 40,
    'ar condicionado' : 2
}

print( dicionario['mouse']  )

dicionario['mouse'] = 39 # Modificando um valor de uma chave

print( dicionario['mouse']  )

dicionario['lousa'] = 3 # Adicionando um elemento

print(dicionario)

dicionario.pop('lousa') # Removendo um elemento

print(dicionario)