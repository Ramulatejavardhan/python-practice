# we reverse the given num by using the mathematical operation.
n=int(input())
s=0
while n>0:
    a=n%10 #it gives the ending number of input. 
    s=s*10+a #multiplies the s with 10 and add the end value of the input to it.
    n=n//10 #removes the ending number from input.
print(s)