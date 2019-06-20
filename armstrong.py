<<<<<<< HEAD
n=int(input("enter the no. u want to check"))
sum=0
tmp=n
while tmp>0:
    digit=tmp%10
    sum+=digit**3
    tmp=int(tmp/10)
print(sum)
if sum == n:
    print("armstrong")
else:
    print("not armstrong")
=======
n=int(input("enter the no. u want to check"))
sum=0
tmp=n
while tmp>0:
    digit=tmp%10
    sum+=digit**3
    tmp=int(tmp/10)
print(sum)
if sum == n:
    print("armstrong")
else:
    print("not armstrong")
>>>>>>> 2ab4ec5da217893e10e6f82d0e0178ebc8b11ab9
