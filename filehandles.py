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
        
