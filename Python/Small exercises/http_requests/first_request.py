import requests
url = "https://news.ycombinator.com/"
response = requests.get(url)

print(response)

#print(response.ok) #boolean value

#print(response.headers) #includes metadata

#print(response.text) #html

#response.status code = status code

