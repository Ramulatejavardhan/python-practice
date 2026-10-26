def my_decorator(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")
    return wrapper
@my_decorator
def hello():
    print("Hello")
hello()