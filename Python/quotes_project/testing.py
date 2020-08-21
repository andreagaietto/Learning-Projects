from bs4 import BeautifulSoup
import requests
response = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")


while soup.select_one(".next") != None:
    next = soup.select_one(".next").find_next().get('href')
    response = requests.get(f"http://quotes.toscrape.com/{next}")
    soup = BeautifulSoup(response.text, "html.parser")
    print(next)



    




""" def get_quote_url(self):
        self.url = self.quote_import.select_one('a').get('href')
        

    def get_author_details(self):
        response = requests.get(f"http://quotes.toscrape.com{self.url}")
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.birthdate = self.soup.select_one(".author-born-date").get_text()
        self.birth_location = self.soup.select_one(".author-born-location").get_text()"""