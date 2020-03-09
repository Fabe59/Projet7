import requests
from config import GOOGLE_MAP_API_KEY


class GoogleMaps:

    def __init__(self):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_coordinates(self, location):
        params = {
            "address" : location,
            "key" : "xxx"
        }

        request = requests.get(self.url, params)
        data = request.json()
        address = data["results"][0]["formatted_address"]
        lat = data["results"][0]['geometry']['location']['lat']
        long = data["results"][0]['geometry']['location']['lng']
        print(address, lat, long)
        #return address, lat, long

def test():
    test = GoogleMaps()
    test.get_coordinates("tour eiffel")

if __name__ == "__main__":
    test()

