class A:

    def f1(self):
        print("Feature 1")

    def f2(self):
        print("Feature 2")

class B:

    def f3(self):
        print("Feature 3")

    def f4(self):
        print("Feature 4")

class C(A,B):

    def f5(self):
        print("Feature 5")

    def f6(self):
        print("Feature 6")

a1=A()
b1=B()
c1=C()

a1.f1()
b1.f4()
c1.f6()