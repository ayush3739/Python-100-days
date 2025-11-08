# Kanye Quotes Generator

A simple GUI application that displays random Kanye West quotes using API integration and Tkinter.

## Features
- **Random Quote Generation**: Fetches random Kanye West quotes from API
- **Simple GUI Interface**: Clean, minimalist design with Kanye's image
- **Click Interaction**: Click Kanye's image to get a new quote
- **API Integration**: Real-time quote fetching from external service

## How It Works
1. Application loads with Kanye's image displayed
2. Click on Kanye's image to fetch a random quote
3. Quote appears in the text area below the image
4. Click again for another random quote

## Files
- `main.py` - Main application with GUI and API integration
- `background.png` - Background image for the application
- `kanye.png` - Kanye West image used as the clickable button

## Technical Implementation
- **Tkinter**: GUI framework for the interface
- **Requests**: HTTP library for API calls
- **JSON Processing**: Parsing API response data
- **Event Handling**: Click events for user interaction

## API Service
Uses the Kanye West quotes API to fetch random quotes in real-time.

## Learning Concepts
- GUI development with Tkinter
- API integration and HTTP requests
- JSON data processing
- Event-driven programming
- Image integration in GUI applications
- Error handling for network requests

## Requirements
- Python 3.x
- tkinter (included with Python)
- requests library
- Internet connection for API access

## Installation
```bash
pip install requests
python main.py
```

## Usage
1. Run the application
2. Click on Kanye's image
3. Enjoy random Kanye quotes!
4. Click again for more quotes

## Customization Ideas
- Add quote saving functionality
- Include different celebrities or quote sources
- Add quote sharing features
- Implement local quote caching
- Add quote favoriting system

Perfect for learning API integration while building a fun, interactive application!