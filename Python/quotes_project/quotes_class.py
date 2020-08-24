from bs4 import BeautifulSoup
import requests


class Quote:
#initialize class to store information about each quote
    def __init__(self, quote_import):
        self.quote_import = quote_import
        self.quote_text = None
        self.author = None
        self.url = None
        self.birthdate = None
        self.birth_location = None
        self.first_first = None
        self.first_last = None
        self.split_name_list = []

    def get_quote_text(self):
        #get text of each quote
        self.quote_text = self.quote_import.select_one(".text").get_text()


    def get_quote_author(self):
        #get author of each quote
        self.author = self.quote_import.select_one(".author").get_text()
        

    def get_quote_url(self):
        #get url with more author information
        self.url = self.quote_import.select_one('a').get('href')
        

    def get_author_details(self):
        #further information on author if needed
        response = requests.get(f"http://quotes.toscrape.com{self.url}")
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.birthdate = self.soup.select_one(".author-born-date").get_text()
        self.birth_location = self.soup.select_one(".author-born-location").get_text()
        

    def get_first_name_letter(self):
        #obtain first letter of first name
        self.split_name_list = self.author.split()
        self.first_first = self.split_name_list[0][0]
        

    def get_last_name_letter(self):
        #obtain first letter of last name
        self.first_last = self.split_name_list[-1][0]
        




        
        