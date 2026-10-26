def my_decorator(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")
    return wrapper