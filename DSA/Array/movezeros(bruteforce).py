arr=[0,1,3,0,0,4,0]
res=[]
for num in arr:
    if num!=0:
        res.append(num)
for i in range(0,len(arr)):
    if arr[i]==0:
        res.append(arr[i])
print(res)