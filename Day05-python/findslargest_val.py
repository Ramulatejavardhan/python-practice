#in this we find the largest value in this list
def larger(lists):
    max=0
    for i in lists:
        if max<i:
            max=i
    return max
print(larger(lists=[3,4,6,8,3]))
print(larger(lists=[9,2,3,5,5]))

#other approach using the built in max function
def larger1(lists1):
    return max(lists1)
print(larger1([1,5,3,10,3]))

