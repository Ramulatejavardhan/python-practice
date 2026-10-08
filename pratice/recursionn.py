def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)
    print(f"Done {n}")
fun(3)