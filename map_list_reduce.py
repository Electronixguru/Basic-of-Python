from functools import *

lst = [10,21,22,34,9,85,2]

even = list(filter(lambda n : n%2==0,lst))
maps = list(map(lambda n : n*2,even))
sum  = reduce(lambda a,b : a+b, maps)
print(even)
print(maps)
print(sum)