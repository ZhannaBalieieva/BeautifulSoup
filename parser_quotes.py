import requests
from bs4 import BeautifulSoup
import json


url = 'https://quotes.toscrape.com'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
data = []
for i in range(0, len(quotes)):
    quot_aut = {quotes[i].text + authors[i].text}
    data.append(quot_aut)
    print(data)
    
    #tagsforquotes = tags[i].find_all('a', class_='tag')
    #for tagforquote in tagsforquotes:
    #    print({tagforquote.text})
    #break


if __name__ == '__main__':
    print(quot_aut)
    with open('quotes.json', 'w', encoding='utf-8') as fd:
       json.dump(quot_aut, fd, ensure_ascii=False)


