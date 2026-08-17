#it stores the value in key value pair
dic={
    "name":"tej",
    "age":19,
}
#accessing the values using the key
val=dic["name"] #or val=dic.get(name)
print(val)

#changing items
dic["age"]=21
x=dic.get("age")
print(x)

#adding new item 
dic["height"]=6
y=dic.get("height")
print(y)

#removing the item
dic.pop("height")
print(dic)