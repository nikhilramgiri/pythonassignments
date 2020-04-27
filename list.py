'''
c=[6,6,9,1]
#print(c)
s=sum(c) #1
#l=len(c)
#mean=s/l
#print(s,l,mean)
print(max(c))#3
#print(c*2)
#help(list)

r=1
for y in c:
    r=r*y
print(r)#2


a=[4,2,6,8,2,]
print(min(a))#4



s=['nik','lol','try','121','5555']#5
c=0
for a in s:
    if a[0]==a[-1]:
        c=c+1
print(c)

def sortSecond(val):#6
    return val[1]
n=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
n.sort(key=sortSecond)
print(n)

p=[6,33,35,6,6,6,8,8,9,9]#7
l=set(p)
p=list(l)


z=[]#8
if len(z)==0:
    print("list is empty")



lst=[10,'nik',52,33,66]#9
list2=lst
print(list2)
print(lst)

no=int(input("enter anuber:"))#10
list1=['nikhil','tejas','Ramgiri','krishnaveni','rock','jim','pam']
list2=[]
for n in list1:
    if len(n)>=no:
        list2.append(n)

print(list2)


def compare(list1,list2):#11
    for n in list1:
        for y in list2:
            if n==y:
                return True
            
            
print(compare([5,3,6,9,8,7],[77,77,99,99,36,66]))


list=[55,66,888,666,4558,7]#12
del(list[0])
print(list)


for x in range(7):#13
    a=(['*'] * x)
    for y in range(5):
        b=[a]*y
        for z in range(4):
            c=([b]* z)
print(c)

#14
list=[4,8,5,3,6,8,95,6,5,6,14,8,22]
list1=[]
for x in list:
    if x%2!=0:
        list1.append(x)

print(list1)


#15
list=[4,8,5,3,6,8,95,6,5,6,14,8,22]
from random import shuffle
shuffle(list)
print(list)


#16 and 17
l=[*range(1,31)]
squareof_l = [a**2 for a in l]

print(squareof_l[:5])
print(squareof_l[-5:])
print(squareof_l[6:31])



#18
import itertools as it
list1=[1,2,3]
print(list(it.permutations(list1)))


#19
l1=[1,11,2,5,4,6,4]
l2=[4,6,10,5,6]
l3=[]
for item in l1:
  if item not in l2:
    l3.append(item)

print(l3)


#20
l= [1,11,2,5,4,6,4]
for i in range(len(l)):
    print("index no.",i,"---","value",l[i])


#21

l=['n','i','k','h','i','l']
for i in range(len(l)):
	print(l[i],end="")


#22
l= [1,11,2,5,4,6,4]
print(l.index(11))

#23
#Not understood
#24
l= [1,11,2,5,4,6,4]
s=['nihil']
a=l+s
print(a)


#25

l= [1,11,2,5,4,6,4]
import random as rd
print(rd.choice(l))

#26

#Not Understood

#27 and 28
l= [1,11,2,5,4,6,4]
l=sorted(l)
print("second smallest---",l[1])
print("second largest---",l[-2])

#29
l= [1,1,3,2,12,1,2,11,2,5,4,6,4]
l=list(set(l))
print(l)

#30
l= [1,1,3,2,12,1,2,11,2,5,4,6,4]
import collections as col
l2=col.Counter(l)
print(l2)


#31
c=0
l= [1,1,3,2,12,1,2,11,2,5,4,6,4]
for i in l:
    if i in range(10,13):
        c=c+1
print(c)
'''
#32
c=0
l= [1,1,3,2,[12,1,2],11,2,[5,4],6,4]
for i in range(len(l)):
    try:
        if len(l[i])>1:
             #print("it contains list")
            print("sublist---",l[i])
    except:
        print(end="")


























































































