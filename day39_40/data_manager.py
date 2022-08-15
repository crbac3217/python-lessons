import requests

SHEETS_URL = "https://api.sheety.co/99cb9c49c3af650202ca63520fe4d4a1/flightDeals/prices"
class DataManager:
    def __init__(self):
        sheets_response = requests.get(url=SHEETS_URL)
        self.sheet_data = sheets_response.json()
    def getCityPrice(self, city):
        for val in self.sheet_data["prices"]:
            if val["city"] == city:
                print(val["lowestPrice"])