import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def get_soup(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, 'html.parser')

    def extract_data(self):
        soup = self.get_soup()
        data = {}
        data['title'] = soup.title.string

        all_links = soup.find_all('a')
        data['links'] = [link.get('href') for link in all_links]

        return data

    def print_data(self):
        data = self.extract_data()
        print("Title:", data['title'])
        print("Links:", data['links'])


if __name__ == "__main__":
    url = "http://example.com"
    scraper = WebScraper(url)
    scraper.print_data()
