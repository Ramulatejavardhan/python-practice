def fac(n):
    if n==0:
        return
    return n*fac(n-1)
print(fac(5))