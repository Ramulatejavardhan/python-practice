arr = [2, 4, 6, 8, 11]
target = 10
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i],",",arr[j])
        else:
            continue