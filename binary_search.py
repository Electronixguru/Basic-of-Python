pos = 0

def search(lst,n):
    l = 0
    u = len(lst)

    while l <=u:
        mid = (l+u)//2
        if lst[mid] ==n:
            globals()["pos"]=mid
            return True
        else:
            if lst[mid]<n:
                l = mid + 1
            else:
                u = mid -1

lst = [10,25,39,40,59,62,74,120]
n = 39

if search(lst,n):
    print("Found at",pos+1)
else:
    print("Not Found")