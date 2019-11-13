'''
parse and get films from html pages
'''
from bs4 import BeautifulSoup
import requests

class CinemaParser:
    def __init__(self, city):
        '''
        srart, create class
        '''
        self.city = city

    def extract_raw_content(self):
        '''
        get html page
        '''
        if self.city == "mck":
            self.content = requests.get("https://msk.subscity.ru")
        else:
            self.content = requests.get("http://spb.subcity.ru")
        self.content = self.content.content.decode("utf-8", errors='ignore')
        return self.content

    def print_raw_content(self):
        '''
        print html page
        '''
        soup = BeautifulSoup(self.extract_raw_content())
        print(soup.prettify())

    def get_films_list(self):
        '''
        get list of films
        '''
        films = []
        soup = BeautifulSoup(self.extract_raw_content())
        span = soup.select(".movie-plates")
        for i in span:
            h = soup.select(".movie-plate")
            for a in h:
                films.append(a.get("attr-title"))
        print(films)


a = CinemaParser("mck")
a.extract_raw_content()
a.print_raw_content()
a.get_films_list()
