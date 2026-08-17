n=int(input())
n=abs(n) #removes the "-ve"
dup=n
revnum=0
while n>0:
    rev=n%10
    revnum=revnum*10+rev
    n=n//10
if revnum==dup:
    print("Palindrome")
else:
    print("Not a palindrome")