list1=[]

p=0
z=0
from random import randint
import random
low=1
high=int(input('high'))#最後一號
for z in range(1, high+1):
    list1.append(z)
aa=len(list1)

list1=random.sample(list1, aa)
print(list1)

a=int(input('a'))#行數
c=0
d=1 

while c<a:
    b=int(input('|b'))#每行人數
        
    for p in range(b):
        print(list1[0], end=" ")
        del list1[0]
    c=c+1
    


