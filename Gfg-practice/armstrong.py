n=int(input())
dup=n
val=0
while n>0:
    s=n%10
    val=val+(s*s*s)
    n=n//10
if dup==val:
    print("True")
else:
    print("False")