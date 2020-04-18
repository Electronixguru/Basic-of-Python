class A:

    def __init__(self):
        print("In init A")

    def f1(self):
        print("Feature 1")

    def f2(self):
        print("Feature 2")

class B:

    def __init__(self):
        print("In init B")

    def f3(self):
        print("Feature 3")

    def f4(self):
        print("Feature 4")

class C(B,A):

    def __init__(self):
        super().__init__()
        print("In init C")

    def f5(self):
        print("Feature 5")

    def f6(self):
        print("Feature 6")

c1=C()

