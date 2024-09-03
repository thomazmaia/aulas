class A:
    def m1(self):
        print("Método M1 de A")

class B(A):
    def m2(self):
        print("Método M2 de B")

class C(A):
    def m2(self):
        print("Método M2 de C")

class D(B,C):
    pass


d = D()
d.m1()
d.m2()