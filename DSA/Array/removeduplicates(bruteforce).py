arr=[1,1,2,2,3]
res=[]
i=0
while i<len(arr):
    if arr[i] in res:
        pass
    else:
        res.append(arr[i])
    i=i+1
print(res)