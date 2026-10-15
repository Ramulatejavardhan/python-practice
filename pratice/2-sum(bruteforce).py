arr=[2,4,6,8,11]
target=1
j=0
for i in range(0,len(arr)):
    if arr[i]+arr[j]==target:
        print(arr[i],",",arr[j])
    else:
        continue