from pyfiglet import Figlet
import requests
import random

f = Figlet(font='slant')
url = "https://icanhazdadjoke.com/search"
again = 'y'
while again != 'n':
    print(f.renderText('Dad Joke 3000'))

    search_term = input("Let me tell you a joke! Give me a topic: ")

    response = requests.get(
        url, 
        headers={"Accept":"application/json"},
        params={"term": search_term}    
    )
    data = response.json()
    result_quantity = len(data["results"]) 
    if result_quantity == 1:
        print(f"I've got one joke about {search_term}. Here it is: ")
        print(data['results'][0]['joke'])
    elif result_quantity > 1:
        print(f"I've got {result_quantity} jokes about {search_term}. Here's one: ")
        index_choice = random.randint(0, result_quantity - 1)
        print(data['results'][index_choice]['joke'])
    else:
        print(f"Sorry, I don't have any jokes about {search_term}. Please try again.")
    again = input("\nWould you like another joke? [y/n]: ")