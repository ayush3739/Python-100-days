class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,origin_code,destination_code,from_time,to_time,price):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price=price
        self.origin_airport=origin_code
        self.destination_airport=destination_code
        self.out_date=from_time
        self.return_date=to_time

def find_cheapest_flights(data):
    if data is None or not data['data']:
        print("No Flights data")
        return FlightData('NA','NA','NA','NA','NA')
        
    # Initialize from the first flight so cheapest_flight is always defined
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    # Correct argument order: origin, destination, out_date, return_date, price
    cheapest_flight = FlightData(origin, destination, out_date, return_date, lowest_price)

    for flight in data['data']:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(origin, destination, out_date, return_date, lowest_price)
            print(f"Lowest price to {destination} is ₹{lowest_price}")
    
    return cheapest_flight




