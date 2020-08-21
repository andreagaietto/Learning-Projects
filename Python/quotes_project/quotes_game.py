from bs4 import BeautifulSoup
import requests
from random import choice
from quotes_class import Quote


object_list = []


def main():
    to_continue = "y"
    response = requests.get("http://quotes.toscrape.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select(".quote")
    for quote in quotes:
        new_quote = Quote(quote)
        object_list.append(new_quote)
        new_quote.get_quote_text()
        new_quote.get_quote_author()
        new_quote.get_quote_url()
    
    
    
    while to_continue != "n":
        quote = choice(object_list)
        print("Here's a quote:")
        print(f"{quote.quote_text}")
        for x in range(4, 0, -1):
            user_guess = input(f"\nWho said this? Guesses remaining: {x}. ")
            if user_guess != quote.author and x == 4:
                quote.get_author_details()
                print(f"Here's a hint: The author was born {quote.birth_location} on {quote.birthdate}.")
            elif user_guess != quote.author and x == 3:
                quote.get_first_name_letter()
                print(f"Here's a hint: The author's first name starts with {quote.first_first}")
            elif user_guess != quote.author and x == 2:
                quote.get_last_name_letter()
                print(f"Here's a hint: The author's last name starts with {quote.first_last}")
            elif user_guess != quote.author and x == 1:
                print(f"I'm sorry, you have used up all of your guesses. The quote author is {quote.author}!")
            else:
                print("You guessed it!")
                break
        to_continue = input("Would you like to continue? (y/n): ")
        if to_continue == "y":
            print("Great! Here we go again...\n")
       

main()
    


