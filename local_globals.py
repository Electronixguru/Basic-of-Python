'''a = 50
def some():
    global a
    a = 9
    print("Local ", a)


some()
print("global ",a)
#output: Local  9, global  9
'''
a=20
b=10
def someone():

   x=globals()['a']
   a = 30
   print("Local ",a)

someone()
print("Global",a)