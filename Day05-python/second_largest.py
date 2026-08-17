def secondlargest(valu):#in lists
    max1=0
    for i in valu:
        if i>max1:
            max1=i
    valu.remove(max1)#we removing the first largest and repeating the above code again
    max2=0
    for i in valu:
        if max2<i:
            max2=i
    return max2
print(secondlargest([1,4,5,7,8]))