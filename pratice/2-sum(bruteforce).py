arr = [2, 4, 6, 8, 11]
target = 10
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i],",",arr[j])
        else:
            continue
# Time complexity:(O(n^2)) in this we use 2 nested loops to find possible ways.
# but it still needs the better version of bruteforce.