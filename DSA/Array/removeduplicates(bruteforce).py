arr=[1,1,2,2,3]
i=0
j=i+1
while arr(i)==len(arr)-1:
    if arr(i)==arr(j):
        arr.remove(arr(j))