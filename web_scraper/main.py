```python
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.website_spider import WebsiteSpider
from web_scraper import settings

def main(url):
    process = CrawlerProcess(settings)
    process.crawl(WebsiteSpider, start_urls=[url])
    process.start()

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    main(url)
```