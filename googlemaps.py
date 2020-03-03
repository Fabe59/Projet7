import requests
from config import GOOGLE_MAP_API_KEY


class GoogleMaps:

    def __init__(self):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_coordinates(self, location):
        params = {
            "address" : location,
            "key" : "AIzaSyByet3QFOJyQq_4e3Rn8shl5SRTb8oXZF4"
        }

        request = requests.get(self.url, params)
        data = request.json()
        address = data["results"][0]["formatted_address"]
        lat = data["results"][0]['geometry']['location']['lat']
        long = data["results"][0]['geometry']['location']['lng']
        return address, lat, long
