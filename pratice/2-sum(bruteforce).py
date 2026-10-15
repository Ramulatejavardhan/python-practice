arr=[2,4,6,8,11]
target=10
j=0
for i in range(0,len(arr)-1):
    if arr[i]+arr[j]==target:
        print(arr[i],arr[i])
    else:
        break