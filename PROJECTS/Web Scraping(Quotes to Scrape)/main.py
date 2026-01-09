from bs4 import BeautifulSoup
import requests

web_site = 'http://quotes.toscrape.com/'
response = requests.get(web_site, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.select_one('h1 a')
quotes = soup.select('div.quote')
if not quotes:
    print(f"Element not found (status={response.status_code}, length={len(response.text)})")
else:
    for quote in quotes:
        text = quote.select_one('span.text')
        author = quote.select_one('small.author')
        if text and author:
            print(f"{text.get_text(strip=True)} — {author.get_text(strip=True)}")

# print(title.get_text(strip=True) if title else "Title not found")