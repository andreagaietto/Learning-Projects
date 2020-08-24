from bs4 import BeautifulSoup
import requests
from random import choice
from quotes_class import Quote


object_list = []


def main():
    to_continue = "y"
    next_page = "y"#assign a value to initialize
    response = requests.get("http://quotes.toscrape.com/") #set initial page to start at
    soup = BeautifulSoup(response.text, "html.parser")
    while next_page != None: #if there is not a next page, expecting to be given a value of None
        quotes = soup.select(".quote") #makes a list of all quote blocks on page
        next_page = soup.select_one(".next") #checks to see if there is a new page button available
        for quote in quotes: #cycles through quotes and creates object for each quote
            new_quote = Quote(quote)#creates object out of each set of needed info
            object_list.append(new_quote)
            new_quote.get_quote_text()
            new_quote.get_quote_author()
            new_quote.get_quote_url()
        if next_page != None:
            next = soup.select_one(".next").find_next().get('href') #pulls url to next page 
            response = requests.get(f"http://quotes.toscrape.com/{next}") #updates next url to use to next page
            soup = BeautifulSoup(response.text, "html.parser") #updates next url to use to next page
    while to_continue != "n":
        #create loop to present quotes until user quits
        quote = choice(object_list)
        print("Here's a quote:")
        print(f"{quote.quote_text}")
        for x in range(4, 0, -1):
            #ask 4 times for guess, giving different hints each time
            user_guess = input(f"\nWho said this? Guesses remaining - {x}: ")
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
        while to_continue not in ("y", "n"):
            to_continue = input("Would you like to continue? (y/n): ")
        if to_continue == "y":
            print("Great! Here we go again...\n")
       

main()
    


