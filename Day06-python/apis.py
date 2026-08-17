import requests
# now the res store the respond of the request we send to server ex:"joke server"then server gives respond the value in the form of json.
res = requests.get("https://official-joke-api.appspot.com/random_joke")
data = res.json()#the .json converts yhe res into json 
print(data["setup"])
print(data["punchline"])