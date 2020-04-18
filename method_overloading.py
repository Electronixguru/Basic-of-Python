class student:

    def sum(self, a=None, b=None, c=None):
        add = 0
        if a !=None and b !=None and c !=None:
            add = a+b+c
        elif a !=None and b !=None:
            add = a+b
        else:
            add = a
        return add

a1 = student()

print(a1.sum(20,30,20))


