arr=[0,0,2,10,23,4,0]
i=0
j=0
while i<len(arr):
    if arr[i]==0:
        i=i+1
    else:
        t=arr[i]
        arr[i]=arr[j]
        arr[j]=t
        j=j+1
print(arr)
# Time complexity:O(n)
# Space complexity:O(1)