def factorial(n):
    val=1
    for i in range(n,0,-1):
        val=val*i
    return val
print(factorial(5))
print(factorial(3))