def example(n):
    for i in range(n):
        for j in range(5):
            print(i, j)
example(3)
# Time complexity:o(n) because inner loop runs only 5 times.