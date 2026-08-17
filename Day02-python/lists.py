items=["apple","bat","cat"]#lists are the muttable that can changeable
print(items[0])
items.append("hello")#it is used to add the add the items at the end of the list
items[1]="ball" #updates the existing index value with new one 
items.pop(0)#removes the items from the list based on the given index if not mentioned removes the last
print(items)
list1=[5,4,3,2,1]
list2=[9,8,7,6]
list1.sort()#sorts them into ascending order
list2.sort()
list1.extend(list2)#combines the both values into the single list
print(list1)