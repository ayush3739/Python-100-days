# Flight Deals Finder

An automated flight price monitoring system that tracks cheap flight deals and sends WhatsApp notifications when prices drop below your target threshold.

## Features
- **Google Sheets Integration**: Manages destination cities and target prices via Sheety API
- **Flight Price Monitoring**: Uses Amadeus API to search for flight deals
- **IATA Code Management**: Automatically fetches and updates airport codes for cities
- **Price Comparison**: Compares current prices with your target thresholds
- **WhatsApp Notifications**: Sends instant alerts via Twilio when deals are found
- **Multi-destination Support**: Monitors multiple destinations simultaneously

## How It Works
1. Reads destination cities and target prices from Google Sheets
2. Fetches IATA airport codes for cities (if not already stored)
3. Searches for flights from origin city to each destination
4. Compares found prices with target prices in spreadsheet
5. Sends WhatsApp notification when cheaper flights are discovered
6. Includes flight details: price, dates, airports, and route information

## Files
- `main.py` - Main application logic and flight monitoring coordination
- `data_manager.py` - Google Sheets API integration via Sheety
- `flight_search.py` - Amadeus flight search API integration
- `flight_data.py` - Flight data structure and cheapest flight finder
- `notification_manager.py` - WhatsApp notifications via Twilio
- `learn.ipynb` - Learning notebook with code experiments
- `readme.md` - This documentation

## Setup Requirements
1. **Google Sheets**: Spreadsheet with cities, IATA codes, and target prices
2. **Sheety API**: Free service to access Google Sheets via REST API
3. **Amadeus Travel API**: Flight search API (free tier available)
4. **Twilio Account**: WhatsApp messaging service
5. **Python Environment**: Python 3.x with required packages

## Environment Configuration
Create `.env` file with:
```
# Sheety API (Google Sheets access)
TOKEN=your_sheety_bearer_token

# Amadeus Flight API
API_KEY=your_amadeus_api_key
API_SEC=your_amadeus_api_secret

# Twilio WhatsApp Integration
ACCOUNT_ID=your_twilio_account_sid
auth_token=your_twilio_auth_token
what_from=your_twilio_whatsapp_number
what_to=recipient_whatsapp_number
```

## Google Sheets Structure
Your spreadsheet should have columns:
- `city` - Destination city name
- `iataCode` - Airport code (auto-populated by the system)
- `lowestPrice` - Your target price threshold
- `id` - Row identifier for Sheety API

## Flight Search Logic
- **Origin**: Configurable origin city (default: NYC)
- **Search Window**: Tomorrow to 7 days from today (customizable)
- **Flight Type**: Round-trip, non-stop flights only
- **Currency**: Indian Rupees (INR) - easily changeable
- **Results**: Top 10 cheapest options per destination

## Notification Features
- **Deal Alerts**: Only notifies when prices drop below your target
- **Detailed Info**: Includes price, route, departure/return dates
- **WhatsApp Integration**: Reliable message delivery
- **Price Comparison**: Shows savings compared to target price

## Example Alert Message
```
🛫 Low price alert! Only ₹45,000 to fly 
from NYC to DEL, 
on 2024-01-15 until 2024-01-22.
```

## Installation  
```bash
pip install requests python-dotenv twilio
python main.py
```

## API Services Used
- **Sheety**: Free Google Sheets API access (up to 1000 requests/month)
- **Amadeus**: Free tier includes 1000 flight searches/month
- **Twilio**: Pay-per-message WhatsApp service with free trial credits

## Customization Ideas
- Change origin city and search timeframe
- Add multiple origin cities for comparison
- Include one-way flight options
- Add email notifications as backup
- Monitor specific airlines or flight classes
- Include hotel and car rental deals
- Add price history tracking

## Learning Concepts
- REST API integration and authentication
- JSON data processing and parsing
- Environment variable security
- Object-oriented programming design
- Error handling and API rate limiting
- Automated notification systems
- Data persistence with external services

## Requirements
- Python 3.x
- requests, python-dotenv, twilio packages
- Internet connection
- Active API accounts (Sheety, Amadeus, Twilio)
- Google Sheets document with destination data

Perfect for learning API integration while building a practical travel tool that can save you money on flights!
