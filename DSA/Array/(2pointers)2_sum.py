arr=[2,4,6,8,11]
target=10
left=0
right=len(arr)-1
while left<right:
    sum=arr[left]+arr[right]
    if sum==target:
        print(arr[left],",",arr[right])
        break
    elif target<sum:#if target thakuva untey total tho manam end pointer ni left ki move
        right=right-1#chestham endhuku antey left move avvuthuntey value thaguthundhi.
    else:
        left=left+1
# Time complexity:O(n)
# Space complexity:O(1)