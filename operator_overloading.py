class addition:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = addition(m1,m2)
        return s3

    def __gt__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        if m1>m2:
            return True
        else:
            return False

a1 = addition(20,23)
a2 = addition(65,30)
a3 = a1 + a2
print(a3.m1)

if a1 > a2:
    print("A1 is greater")
else:
    print("A2 is greater")











