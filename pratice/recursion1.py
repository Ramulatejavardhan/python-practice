def count(n):
    if n==0:
        return
    count(n-1)
    print(n)
count(5)
"""A. Base case:
The condition that stops further recursive calls.
if n == 0:
    return
Without a reachable stopping condition, calls can continue until Python raises a RecursionError.

B. Recursive case:
The part where the function calls itself with a new input.
count(n - 1)

The input changes from 3 to 2, then 1, then 0. It moves toward the base case."""