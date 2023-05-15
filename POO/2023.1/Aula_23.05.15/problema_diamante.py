class ClassA:
    def m1(self):
        print("Métdo M1")


class ClassB(ClassA):
    def m2(self):
        print("Métdo M2 - B")


class ClassC(ClassA):
    def m2(self):
        print("Métdo M2 - C")


class ClassD(ClassC, ClassB):
    pass


teste = ClassD()
teste.m1()
teste.m2()
