# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.rithmschool.com/blog')
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')

with open('blog_data.csv', 'w') as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(['title', 'link', 'date'])

	for article in articles:
		a_tag = article.find('a')
		title = article.find('a').get_text()
		url = article.find('a')['href']
		date = article.find('time')['datetime']
		csv_writer.writerow([title, url, date])

