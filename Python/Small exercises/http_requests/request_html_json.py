import requests

url = "https://icanhazdadjoke.com/"

#response = requests.get(url, headers={"Accept":"text/plain"})
#doesn't work with every website
#print(response.text)

response = requests.get(url, headers={"Accept":"application/json"})
print(response.text) #looks like a dict but is a string
data = response.json() #returns a python dict

#print(type(data)) #proves type dict

print(data["joke"])