import os 
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv(".env")

TOKEN=os.getenv("TOKEN")
sheety_headers={
    "Authorization": f"Bearer {TOKEN}"
}




class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url="https://api.sheety.co/34b68a6debe76b0bdf371fb057e52483/flightDeals/prices"
        self.get_data()
        
    def get_data(self):
        
        response=requests.get(url=self.sheety_url,headers=sheety_headers)
        self.data=response.json()["prices"]
        return self.data
    
    def update_iata(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # Fix: update each row inside the loop
            response = requests.put(
                url=f"{self.sheety_url}/{city['id']}",
                json=new_data,
                headers=sheety_headers
            )
            print(response.text)





