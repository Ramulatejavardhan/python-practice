def val(n):
    if n==0:
        return
    else:
        val(n-1)
        print(n)
val(5)