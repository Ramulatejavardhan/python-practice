#the "try" used to test the block of codes for errors
try:
    print(x)
except NameError:#the "NameError" it runs if the vaiable is not defined
    print("variable is not defined")
else:#if no error occured this code will execute
    print('nothing went wrong')
finally:
    print("it will even error occured")

#raise exception is used to raise the exception if error occured
n=-1
if n<0:
    raise Exception("the value is lessthan the 0")
