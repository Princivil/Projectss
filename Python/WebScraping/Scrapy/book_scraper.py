# https://books.toscrape.com/

import scrapy # had issues running scrapy in terminal

class BookSpider(scrapy.Spider):
	name = 'BookSpider'
	start_urls = ['https://books.toscrape.com/'] # Does the requests.get automatically

	def parse(self, response):
		 for article in response.css("article.product_pod") # all articles with product pod specification
		 	yield {
		 	"price": article.css("product_color::text").extract_first(),
		 	# reps an a tag inside h3 with attribute title
		 	"title": article.css("h3 > a::attr(title)").extract_first()
		 	}
		 	next = response.css(".next > a::attr(href").extract_first()
		 	if next:
		 		yield response.follow(next, self.parse)


