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
