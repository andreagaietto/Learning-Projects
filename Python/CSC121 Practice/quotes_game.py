from bs4 import BeautifulSoup
import requests

response = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")


"""quotes = soup.select(".text")
for x in quotes:
    print(x.get_text())
    gets all of the quotes"""

test = soup.select(".quote")
print(len(test))

