from functools import reduce
l1=[1,2,3,4,5,6,7,8]
a=reduce(lambda x,y:x+y,l1)
print(a)
# print(list(map(lambda x, y:x+y,l1)))