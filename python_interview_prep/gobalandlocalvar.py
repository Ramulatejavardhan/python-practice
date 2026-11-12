def outer():
    count = 10
    def inner():
        nonlocal count
        count = 20
    inner()
    print(count)
outer()