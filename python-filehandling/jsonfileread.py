import json
filepath="person.json"
with open(filepath,"r")as file:
    cont=json.load(file)
    # print(cont["age"])
    print(cont)