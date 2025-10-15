# Day 45 - Web Scraping with Beautiful Soup

This folder contains web scraping projects and learning materials using the Beautiful Soup library for parsing HTML and extracting data from websites.

## 📁 Files Overview

### Beautiful Soup Start
Located in `bs4-start/` folder:
- **`main.py`** - Introduction to Beautiful Soup with multiple examples
- **`website.html`** - Sample HTML file for practice scraping

### 🎬 100 Movies to Watch Project
Located in `100 movies to watch start/` folder:
- **`main.py`** - Web scraper for Empire's top 100 movies list
- **`Movies.txt`** - Output file containing the scraped movie titles
- **`README.md`** - Detailed project instructions and objectives

## 🎯 Topics Covered

### 1. Beautiful Soup Basics
- Installing and importing BeautifulSoup4
- Parsing HTML with different parsers (`html.parser`)
- Navigating the HTML tree structure
- Using `prettify()` to format HTML output

### 2. Finding Elements
- **`find()`**: Find the first matching element
- **`find_all()`**: Find all matching elements
- Searching by tag name (e.g., `name="h3"`)
- Searching by class (e.g., `class_="title"`)
- Searching by id (e.g., `id="name"`)
- Attribute selection

### 3. Extracting Data
- **`getText()`**: Extract text content from elements
- **`get()`**: Extract attribute values (e.g., `href`, `src`)
- List comprehensions for bulk data extraction
- Text processing and formatting

### 4. CSS Selectors
- **`select_one()`**: Select using CSS selector (single element)
- **`select()`**: Select using CSS selector (multiple elements)
- Complex selector syntax (e.g., `"p a"` for anchor inside paragraph)

### 5. Web Scraping with Requests
- Using the `requests` library to fetch web pages
- Setting custom headers for web requests
- Handling HTTP responses
- Scraping live websites (e.g., Hacker News)

## 🎯 Project Features

### Beautiful Soup Start (`bs4-start/main.py`)
Demonstrates:
- Parsing local HTML files
- Finding and extracting anchor tags
- Working with headings and classes
- CSS selector usage
- Scraping Hacker News for articles with most upvotes
- Finding article titles, links, and vote counts
- Identifying the highest-voted article

### 100 Movies Project (`100 movies to watch start/main.py`)
Demonstrates:
- Scraping archived web pages (Internet Archive Wayback Machine)
- Extracting movie titles from HTML
- Reversing list order (ascending order)
- Writing data to a text file
- File handling with UTF-8 encoding

## 🔗 External Resources Used

### Libraries
- **BeautifulSoup4**: HTML/XML parsing library
- **requests**: HTTP library for Python
- Installation: `pip install beautifulsoup4 requests`

### Websites Scraped
- **Empire Online**: Top 100 movies list (via Internet Archive)
  - URL: `https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/`
- **Hacker News**: Tech news aggregator
  - URL: `https://news.ycombinator.com/news`

## 📚 Documentation Links

### Beautiful Soup
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Beautiful Soup Quick Start](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)
- [Searching the Tree](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree)

### Requests Library
- [Requests Documentation](https://docs.python-requests.org/)
- [Requests Quickstart](https://docs.python-requests.org/en/latest/user/quickstart/)

### Python File Handling
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [UTF-8 Encoding](https://docs.python.org/3/howto/unicode.html)

## 🚀 Getting Started

### Installation
```bash
pip install beautifulsoup4 requests
```

### Running the Projects

#### Beautiful Soup Start
```bash
cd "Day 45/bs4-start"
python main.py
```

#### 100 Movies Project
```bash
cd "Day 45/100 movies to watch start"
python main.py
```

## 📝 Key Learning Points

- Web scraping fundamentals with Beautiful Soup
- Parsing HTML and navigating the DOM tree
- Finding elements by tag, class, and id
- Extracting text and attributes from HTML elements
- Using CSS selectors for complex queries
- Making HTTP requests to fetch web pages
- Handling text encoding (UTF-8)
- Writing scraped data to files
- Processing and transforming scraped data
- Working with archived web pages to ensure consistency
- Best practices for web scraping (respecting robots.txt, rate limiting)

## ⚠️ Important Notes

- Always check a website's `robots.txt` and terms of service before scraping
- Use the Internet Archive's Wayback Machine URL for the movies project to ensure consistency
- Be respectful of websites: don't overwhelm servers with too many requests
- Some websites may block scraping attempts; always scrape responsibly
