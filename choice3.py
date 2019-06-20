<<<<<<< HEAD
n=int(input("choice"))
di=dict()
for i in range(0,n):
    v=input("string")
    if v[0] not in di:
        di[v[0]]=[]
    di[v[0]].append(v)
ch=input("choice")
if ch in di:
    print(di[ch])
=======
n=int(input("choice"))
di=dict()
for i in range(0,n):
    v=input("string")
    if v[0] not in di:
        di[v[0]]=[]
    di[v[0]].append(v)
ch=input("choice")
if ch in di:
    print(di[ch])
>>>>>>> 2ab4ec5da217893e10e6f82d0e0178ebc8b11ab9
