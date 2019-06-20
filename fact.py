
while True:
    n=int(input("enter the choice less than 7 more than 2"))
    if n>2 and n<=7:
        break

pd=dict()
cp=0
p=2
while cp<=n:

    check=0
    for i in range(2,p-1):
        if p%i is 0:
            check=1
    if check is 0:
        pd[p]=1
        for j in range(1,p+1):
            pd[p]=pd[p]*j
        cp+=1    
    p+=1
ch=int(input("enter the choice"))
if ch in pd:
    print(pd[ch])
print(pd)    
    
    

