arr=[2,4,6,8,11]
target=15
left=0
right=len(arr)-1
while left<right:
    total=arr[left]+arr[right]
    if total==target:
        print(arr[left],",",arr[right])
        break
    elif total<arr[right]:
        right=right-1
    else:
        left=left+1