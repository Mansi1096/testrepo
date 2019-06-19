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
