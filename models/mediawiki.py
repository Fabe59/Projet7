import requests


class Mediawiki:

    def __init__(self):
        self.url = "https://fr.wikipedia.org/w/api.php"
        

    def get_page_id(self, latitude, longitude):
        coordinates = f"{latitude}|{longitude}"
        params = {
            "action" : "query",
            "list" : "geosearch",
            "gsradius" : 100,
            "gscoord" : coordinates,
            "format" : "json"
        }
        
        request = requests.get(self.url, params)
        data = request.json()
        pageid = data['query']['geosearch'][0]['pageid']
        return pageid

    def extract_info(self, pageid):
        params = {
            "format" : "json",
            "action" : "query",
            "prop" : "extracts|info",
            "inprop" : "url",
            "exsentences" : 5,
            "explaintext" : True,
            "pageids" : pageid
        }

        request = requests.get(self.url, params)
        data = request.json()
        info = data["query"]["pages"][str(pageid)]["extract"]
        url = data["query"]["pages"][str(pageid)]["fullurl"]

