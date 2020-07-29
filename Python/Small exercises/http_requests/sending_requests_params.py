import requests

# basic method response = requests.get("http://www.example.com", params={"key1": "value1", "key2": "value2"})

url = "https://icanhazdadjoke.com/search"



response = requests.get(
    url, 
    headers={"Accept":"application/json"},
    params={"term": "cat"}    
)
data = response.json() 



print(data)