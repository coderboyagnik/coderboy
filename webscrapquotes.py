import requests
from bs4 import BeautifulSoup

def get_quotes():
    response = requests.get("http://quotes.toscrape.com")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")
    for quote in quotes:
        print(quote.text)

if __name__ == "__main__":
    get_quotes()
