from settings.config import key_google_geocoding_api
import requests


class GoogleMaps:

    def __init__(self):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_coordinates(self, location):
        """ Getting the coordinates and address of the place """
        params = {
            "address": location,
            "key": key_google_geocoding_api
        }

        request = requests.get(self.url, params)
        data = request.json()
        address = data["results"][0]["formatted_address"]
        lat = data["results"][0]['geometry']['location']['lat']
        long = data["results"][0]['geometry']['location']['lng']
        return address, lat, long
