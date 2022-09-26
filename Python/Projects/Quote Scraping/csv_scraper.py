# http://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = 'http://quotes.toscrape.com'


def scrape_quotes():
    # create list to append quotes
    url = '/page/1'
    all_quotes = []
    # Web Scraping portion
    while url:
        res = requests.get(f'{base_url}{url}')
        print(f'Now Scraping: {base_url}{url}...')
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all(class_='quote')

        for quote in quotes:
            all_quotes.append({
                'text': quote.find(class_='text').get_text(),  # want inner text not span
                'author': quote.find(class_='author').get_text(),
                'bio': quote.find('a')['href']
            })
        next_btn = soup.find(class_='next')
        url = next_btn.find('a')['href'] if next_btn else None
        sleep(1)
    return all_quotes


def write_quotes(quotes):
    with open('quotes.csv', 'w') as file:
        headers = ['text', 'author', 'bio']
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes(quotes)
