'''
parse and get films from html pages
'''
from bs4 import BeautifulSoup
import requests

class CinemaParser:
    def __init__(self, *city):
        '''
        srart, create class
        '''
        self.city = city
        self.content = ""

    def extract_raw_content(self):
        '''
        get html page
        '''
        if self.city == "msk":
            self.content = requests.get("https://msk.subscity.ru")
        elif self.city == "spb":
            self.content = requests.get("http://spb.subcity.ru")
        else:
            self.content = requests.get("https://msk.subscity.ru")
        self.content = self.content.content.decode("utf-8", errors='ignore')
        return self.content

    def print_raw_content(self):
        '''
        print html page
        '''
        soup = BeautifulSoup(CinemaParser.extract_raw_content(self))
        print(soup.prettify())

    def get_films_list(self):
        '''
        get list of films
        '''
        films = []
        soup = BeautifulSoup(CinemaParser.extract_raw_content(self))
        span = soup.select(".movie-plates")
        for i in span:
            h = soup.select(".movie-plate")
            for a in h:
                films.append(a.get("attr-title"))
        print(films)


a = CinemaParser()
#a.extract_raw_content()
#a.print_raw_content()
a.get_films_list()

