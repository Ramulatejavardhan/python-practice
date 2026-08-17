#function is a reusability of a code without typing it again
def func():
    print("hi")
func()
func()
func()
#global variable and local variable
globalv=10#global var
def function():
    globalv=11#local var
    print(globalv)#prints the local var
function()
print(globalv)#The global variable prints because the local variable works only in inside of the function
#if local val has to to print in outside of function we have to use the "global var name"
globalv=99
def function():
    global globalv
    globalv=101
    print(globalv)
function()
print(globalv)

#function arguments
def math(a,b):#this are parameters example of the values
    print(a+b)
math(1,2)
math(22,22)