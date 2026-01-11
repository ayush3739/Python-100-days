from flask import Flask, request, render_template, jsonify
import requests,os,json,datetime
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
api_key=os.getenv('API_KEY')



def stock_call(name):
    parameter={
            'apikey':api_key,
            'function':'TIME_SERIES_DAILY',
            'symbol':name,
            'outputsize':'compact',
            'datatype':'json',
            'outputsize':'compact'
        }

    response=requests.get(STOCK_ENDPOINT,params=parameter)
    response.raise_for_status()
    stock_data=response.json()
    
    with open('stock_json.json','w') as file:
        json.dump(stock_data,file,indent=4)

    return stock_data

def check_dates():
    with open('stock_json.json','r') as file:
        stock_data=json.load(file)

    ct=stock_data['Meta Data']['3. Last Refreshed']
    dt = str(datetime.date.today() - datetime.timedelta(days=2))
    if ct!=dt:
        return False
    else:
        return stock_data

if check_dates()==False:
    print('date delay') 
    stock_data=stock_call('IBM')
else:
    stock_data = check_dates()
    print('no date delay')

# if __name__ == "__main__":
#     app.run(debug=True)
