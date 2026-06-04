n=int(input())
s=0
while n!=0: #"Number lo digits unna varaku continue avuthundhi."
    l=n%10 #10 tho divide chesthe remainder = last digit vasthundhi.
    s=s+l  
    n//=10  #removes the last digit by using floor division.
print(s)