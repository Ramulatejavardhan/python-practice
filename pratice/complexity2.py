def find_pair(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == 10:
                return True
    return False
print(find_pair([2, 4, 6, 8, 11]))
# time complexity: