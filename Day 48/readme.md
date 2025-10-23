# Day 48 - Selenium Web Automation

## Overview
This project demonstrates web automation using Selenium WebDriver with Python. It includes multiple exercises to learn browser automation, element interaction, and web scraping.

## Projects Included

### 1. Cookie Clicker Bot (main.py)
An automated bot that plays the Cookie Clicker game by:
- Clicking the cookie repeatedly
- Automatically purchasing the best available upgrade every 5 seconds
- Running for 5 minutes and reporting final score
- Uses intelligent buying strategy by checking enabled items

**Key Features:**
- Automated cookie clicking
- Smart upgrade purchasing based on availability
- Time-based automation (5-minute runtime)
- Error handling for missing elements

### 2. Form Filling Challenge (challenge.py)
Automated form submission script that:
- Navigates to a form page
- Fills in first name, last name, and email fields
- Automatically submits the form

**Key Features:**
- Element location by NAME attribute
- Form data input automation
- Button click automation

### 3. Wikipedia Interaction (interact.py)
Interactive web automation demonstrating:
- Navigating to Wikipedia
- Finding elements by XPath and Link Text
- Search functionality using keyboard input
- Browser window management

**Key Features:**
- Multiple element location strategies
- Keyboard input simulation
- Link clicking
- Search functionality

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Python 3**: Programming language
- **Chrome WebDriver**: Chrome browser automation

## Key Concepts Learned
1. Setting up Selenium WebDriver
2. Finding elements using different locators (XPath, CSS Selector, Name, Link Text)
3. Clicking elements
4. Sending keyboard input
5. Exception handling in web automation
6. Time-based automation
7. Chrome options configuration

## Prerequisites
```bash
pip install selenium
```

## Setup
1. Install Selenium: `pip install selenium`
2. Ensure Chrome browser is installed
3. ChromeDriver will be automatically managed by Selenium

## Usage

### Cookie Clicker Bot
```bash
python main.py
```

### Form Filling Challenge
```bash
python challenge.py
```

### Wikipedia Interaction
```bash
python interact.py
```

## Notes
- `chrome_options.add_experimental_option("detach", True)` keeps the browser open after script completion
- The Cookie Clicker game runs for 5 minutes before displaying results
- All scripts use Chrome browser by default
