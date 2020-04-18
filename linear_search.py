pos = -1
def search(lst,n):
    i = 0
    for i in range(i,len(lst)) :
        if lst[i] == n:
            globals()["pos"] = i
            return True
    return False

lst = [10,2,4,6,12,7]
n = 4

if search(lst,n):
    print("Found at ",pos+1)
else:
    print("Not Found")