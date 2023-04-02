class Ponto:
    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

    def setX(self, x):
        if x > 0:
            self.__x = x
    
    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y



P = Ponto(5, 10)
print(P.getX(), P.getY())

P.setX(-20)
P.setY(30)

print(P.getX(), P.getY())