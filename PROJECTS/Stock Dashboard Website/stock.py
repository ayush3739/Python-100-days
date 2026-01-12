import requests,os,json,time    
from datetime import datetime, timedelta, date
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
api_key=os.getenv('API_KEY')

stocks_comp=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "RELIANCE.BSE", "INFY.BSE"]

os.makedirs("cache", exist_ok=True)

def _cached_symbols():
    out = []
    for p in Path("cache").glob("*.json"):
        sym = p.stem.strip().upper()
        if sym:
            out.append(sym)
    return out

stocks_comp = list(dict.fromkeys([s.strip().upper() for s in stocks_comp] + _cached_symbols()))

def stock_fetch(name):
    parameter={
            'apikey':api_key,
            'function':'TIME_SERIES_DAILY',
            'symbol':name,
            'outputsize':'compact',
            'datatype':'json',
        }

    response=requests.get(STOCK_ENDPOINT,params=parameter)
    response.raise_for_status()
    return response.json()

def stock_call(name):
    stock_data=stock_fetch(name)

    if ("Time Series (Daily)" not in stock_data) or ("Meta Data" not in stock_data) or ("Note" in stock_data) or ("Error Message" in stock_data) or ("Information" in stock_data):
        return stock_data
    
    with open(f'cache/{name}.json','w') as file:
        json.dump(stock_data,file,indent=4)

    return stock_data

def last_trading_day():
    today = date.today()
    weekday = today.weekday()

    if weekday >= 5:
        offset = weekday - 4
        return (today - timedelta(days=offset)).isoformat()
    else:
        return today.isoformat()
    
def prev_trading_day():
    today = date.today()
    weekday = today.weekday()

    if weekday == 0:
        return (today - timedelta(days=3)).isoformat()
    elif weekday >= 1 and weekday <= 4:
        return (today - timedelta(days=1)).isoformat()
    else:
        offset = weekday - 4
        return (today - timedelta(days=offset)).isoformat()
    
def check_dates(symbol):
    try:
        with open(f'cache/{symbol}.json','r') as file:
            stock_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    if "Time Series (Daily)" not in stock_data or "Meta Data" not in stock_data:
        return False

    ct = stock_data['Meta Data']['3. Last Refreshed'].split()[0]

    ltd = last_trading_day()
    ptd = prev_trading_day()

    if ct == ltd or ct == ptd:
        return stock_data
    return False

if __name__ == "__main__":
    symbol = 'RELIANCE.BSE'
    for i in stocks_comp:
        cached = check_dates(i)  

        if not cached:
            print("Cache outdated or missing — fetching fresh")
            stock_data = stock_call(symbol)
        else:
            print("Using cached data")
            stock_data = cached
        time.sleep(2)
