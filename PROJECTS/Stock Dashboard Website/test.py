from dotenv import load_dotenv
import os, requests, json,time
load_dotenv()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
api_key = os.getenv('API_KEY')

stocks_comp = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "RELIANCE.BSE", "INFY.BSE"]

def fetch_quotes(symbols):
    all_quotes = {}

    for sym in symbols:
        params = {
            'apikey': api_key,
            'function': 'GLOBAL_QUOTE',
            'symbol': sym
        }

        print(f"Fetching {sym}...")
        response = requests.get(STOCK_ENDPOINT, params=params)
        data = response.json()

        # Check if the API returned valid data
        if "Global Quote" in data and data["Global Quote"]:
            all_quotes[sym] = data["Global Quote"]
        else:
            all_quotes[sym] = {"error": "No data returned"}
        time.sleep(2)

    # Save once
    with open('Global_Quotes.json', 'w') as file:
        json.dump(all_quotes, file, indent=4)

    return all_quotes

fetch_quotes(stocks_comp)
