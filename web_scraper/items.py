```python
from scrapy import Item, Field

class WebsiteScraperItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    title = Field()
    content = Field()
```