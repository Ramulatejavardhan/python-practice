arr = [4, 2, 4, 1, 2, 5]
res=[]
i=0
# while i<len(arr): we can use both types of loops in this problem.
for i in range(i,len(arr)):
    if arr[i] in res:
        pass
    else:
        res.append(arr[i])
    # i=i+1
print(res)
"""In this we use the another array to move the values to if the value already exist we leave that
and move to another value like wise so that we can get unique values in the list or array."""
#Time-complexity:O(n^2)
#space-complexity:O(n)