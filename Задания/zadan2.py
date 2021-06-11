import math

mylist = [0, 10, -6, -3, 2, 1]
a = list(map(lambda x: abs(x), mylist[mylist.index(0):] ))
print(sum(a), min(a[a.index(1):]))
