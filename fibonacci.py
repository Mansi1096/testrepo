n=int(input("print number of terms"))
a,b,c=0,1,0
print(a)
print(b)
for i in range(0,n-2):   
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
