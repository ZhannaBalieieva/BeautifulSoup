import requests
from bs4 import BeautifulSoup
import json
import re

BASE_URL = 'https://quotes.toscrape.com'


def parse_authors(url_authors: list[str]) -> list[dict]:
    authors = []

    for url_author in url_authors:
        # потрібно посилання користувача, яке ви отримали раніше, поєднати із базовим url та зробити запит для отримання автора
        url = BASE_URL + url_author
        html_doc = requests.get(url)

        if html_doc.status_code != 200:
            print(f"Error status code: {html_doc.status_code} | Url author: {url_author}")
            continue

        soup = BeautifulSoup(html_doc.content, 'html.parser')
        author = soup.select("div[class=author-details]")[0]

        authors.append(
            {
                "fullname": author.find('h3', attrs={"class": "author-title"}).text.split('\n', maxsplit=1)[0].strip(),
                "born_date": author.find('span', attrs={'class': 'author-born-date'}).text.strip(),
                "born_location": author.find('span', attrs={'class': 'author-born-location'}).text.strip(),
                "description": author.find('div', attrs={'class': 'author-description'}).text.strip()
            }
        )

    return authors


def parse_quotes() -> tuple[list, list]:
    html_doc = requests.get(BASE_URL)
    if html_doc.status_code != 200:
        raise Exception(f"Error status code: {html_doc.status_code}")

    quotes = []
    url_authors = []

    soup = BeautifulSoup(html_doc.content, 'html.parser')
    for quote in soup.select("div[class=quote]"):
        quotes.append(
            {
                "quote": quote.find("span", attrs={"class": "text"}).text.strip(),
                "author": quote.find("small", attrs={"class": "author"}).text.strip(),
                "tags": [tag.text.strip() for tag in quote.find("div", attrs={"class": "tags"}).find_all('a')],
            }
        )
        url_authors.append(quote.select('span a')[0]['href'])

    authors = parse_authors(url_authors)

    return quotes, authors


if __name__ == '__main__':
   quotes, authors = parse_quotes()

   print(quotes)
   print(authors)
   with open('authors.json', 'w', encoding='utf-8') as fd:
       json.dump(authors, fd, ensure_ascii=False)