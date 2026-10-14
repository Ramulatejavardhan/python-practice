def find_pair(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == 10:
                return True
    return False
print(find_pair([2, 4, 6, 8, 11]))
""" time complexity:o(n^2)
\(O(n^2)\) endhukante outer loop \(n\) times run avuthundhi, inner loop kuda total ga approximately \(n\) times per outer iteration work chesthundhi, so total work \(n \times n = n^2\)"""