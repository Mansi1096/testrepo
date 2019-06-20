n=int(input("choice"))
di=dict()
for i in range(0,n):
    v=input("enter string")
    di[v[0]]=v
    choice=input("str choice")
    if choice in di:
        print(di[choice])
    else:
        print("no string matched")
