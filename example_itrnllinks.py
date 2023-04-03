from typing import List
import requests
from bs4 import BeautifulSoup
import json
import urllib

###########внутренние ссылки##########

response = requests.get('https://quotes.toscrape.com/') 
soup = BeautifulSoup(response.content, 'html.parser') 

#Вывод всех ссылок:
#internalLinks = [ 
#    a.get('href') for a in soup.find_all('a') 
#    if a.get('href') and a.get('href').startswith('/')] 
#print(internalLinks) 

links = [a.get('href') for a in soup.find_all('a')]
to_extract = ["author"]
author_links = []
for link in links:
    data = []
    for author in to_extract:
        if link and author in link:
            author_links.append(link)
            for link in author_links:
                result = {link}
                data.append(result)
                #print(data)
print(author_links)


def spider(author_links: List[str]):
    data = []
    for author in author_links:
        response = requests.get('https://quotes.toscrape.com/') 
        soup = BeautifulSoup(response.content, 'html.parser')
        if link and author in link:
            author_links.append(link)
            print(author_links)
        for author in author_links:
            result = {}
        data.append(result)
        
    


#if __name__=='__main__':
#    result = author_links()
#    print(result)