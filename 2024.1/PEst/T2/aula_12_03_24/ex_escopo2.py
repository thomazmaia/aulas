def minha_funcao():
    var = 5
    print(var)

def outra_funcao():
    global var
    var = 5
    print(var)

var = 10
minha_funcao()
print(var)
outra_funcao()
print(var)