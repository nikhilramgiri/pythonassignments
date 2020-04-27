#1
'''
a=1
b=2
for i in range(1,4):
    k=0
    for j in range(1,b+1):
        print(" ",end="")
    for j in range(1,a+1):
        if j<=i:
            k=k+1
        else:
            k=k-1
        print(k,end="")
    print()
    a=a+2
    b=b-1
 
#2
for i in range(1,4):
    print(" "*(3-i),end="")
    for j in range(1,i):
        print(i-j,end="")
    for k in range(0,i):
        print(k,end="")
    print()
'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if j%2==0:
            print(2,end="")
        else:
            print(1,end="")
    for k in range(i-1,0,-1):
        if k%2==0:
            print(2,end="")
        else:
            print(1,end="")
        #print(k,end="")
    print()
