import requests

sheety_endpoint = "https://api.sheety.co/8770d1eda53a01f2846505862b8a3d48/копияFlightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):
        data = requests.get(url=sheety_endpoint).json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data
    
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.post(url=f"{sheety_endpoint}/{city['id']}", json=new_data)
            print(response.text)
            