```python
import scrapy
from scrapy.http import Request
from web_scraper.items import Item

class WebsiteSpider(scrapy.Spider):
    name = 'website_spider'
    allowed_domains = ['example.com']  # Replace with the domain of the website you want to scrape
    start_urls = ['http://example.com/']  # Replace with the URL of the website you want to scrape

    def parse(self, response):
        item = Item()

        # Extract data from the page and assign it to the item
        # This will depend on the structure of the website
        # For example:
        # item['title'] = response.css('h1::text').get()
        # item['content'] = response.css('div.content::text').get()

        yield item

        # Handle pagination
        # This will depend on the structure of the website
        # For example:
        # next_page = response.css('a.next::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)

    def handle_spider_closed(self, spider):
        # This method is called when the spider is closed
        # You can put any cleanup code here
        pass
```