def funcao1():
    X = 10
    print(X)
    funcao2()
    print(X)
    
def funcao2():
    global X
    X = 20
    print(X)

X = 0
print(X)
funcao1()
print(X)
funcao2()
print(X)