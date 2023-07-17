```python
import re

def extract_domain(url):
    """
    Extracts domain from a given url
    """
    domain = re.search('https?://([A-Za-z_0-9.-]+).*', url)
    if domain:
        return domain.group(1)
    return None

def is_absolute(url):
    """
    Checks if a given url is absolute
    """
    return bool(re.match('^[a-z]+://', url))
```