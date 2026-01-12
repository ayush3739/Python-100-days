# 📜 Web Scraping - Quotes to Scrape

A Python web scraper that extracts quotes and their authors from [quotes.toscrape.com](http://quotes.toscrape.com/) using BeautifulSoup and requests.

## ✨ Features

- **Quote Extraction**: Scrapes all quotes from the homepage
- **Author Attribution**: Captures the author for each quote
- **Clean Output**: Formats quotes as "Quote text — Author"
- **Error Handling**: Validates response status and checks for missing elements

## 🚀 How to Use

1. Install dependencies:
   ```bash
   pip install beautifulsoup4 requests
   ```

2. Run the scraper:
   ```bash
   python main.py
   ```

3. View extracted quotes in the console

## 🛠️ Technical Details

### Scraping Process

```python
# 1. Send GET request to website
response = requests.get(url, timeout=10)

# 2. Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Select quote containers
quotes = soup.select('div.quote')

# 4. Extract text and author from each quote
text = quote.select_one('span.text')
author = quote.select_one('small.author')
```

### Key Components

- **BeautifulSoup**: HTML parsing and element selection
- **requests**: HTTP requests with timeout and status validation
- **CSS Selectors**: `div.quote`, `span.text`, `small.author`

## 📦 Requirements

```
beautifulsoup4
requests
```

## 💡 Learning Concepts

- Web scraping fundamentals
- HTML parsing with BeautifulSoup
- CSS selector usage
- HTTP request handling
- Error handling in web scraping
