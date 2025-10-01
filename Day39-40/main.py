#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import find_cheapest_flights
from flight_search import FlightSearch
from notification_manager import NotificationManager
import time
from datetime import datetime, timedelta

tomorrow=datetime.now()+timedelta(days=1)
six_months_from_today=datetime.now()+timedelta(days=(7))

dt=DataManager()
sheet_data=dt.get_data()
print(sheet_data)
flight_search = FlightSearch()


# flight_data=FlightData()

origin_city_code="NYC"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    time.sleep(2)
    print(f"sheet_data:\n {sheet_data}")

    dt.data = sheet_data
    dt.update_iata()




# ==================== Search for Flights ====================
for destination in sheet_data:
    print(f"Getting Flights for {destination['city']}...")
    flights=flight_search.check_flights(
        origin_code=origin_city_code,
        destination_code=destination['iataCode'],  # fix: use current destination
        from_time=tomorrow,
        to_time=six_months_from_today)

    cheapest_flight = find_cheapest_flights(flights)
    if cheapest_flight and cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # SMS not working? Try whatsapp instead.
        notification_manager = NotificationManager()
        notification_manager.send_notification(
            message_body=f"Low price alert! Only ₹{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
    print(f"from:{origin_city_code} to {destination['city']} on {cheapest_flight.out_date} for ₹{cheapest_flight.price}")

    time.sleep(2)


