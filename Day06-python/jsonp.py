#json is javascript object notation
import json #it is a built in package
a='{"name":"tej","age":19}'#it is not a dictionary it is javascript object
#to convert the json into the python dictionary
b=json.loads(a)
print(type(b))
print(b["name"])

#conveting back into dictionary to json
c = json.dumps(b)# converted back into json
print(type(c))