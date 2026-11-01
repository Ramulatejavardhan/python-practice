#*args The allows a function to accept any number of positional arguments.
#Python collects those arguments into a tuple.
def val(*args):
    print(args)
val(10,20,30)