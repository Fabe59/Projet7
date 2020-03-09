import requests


class Mediawiki:

    def __init__(self):
        self.url = "https://fr.wikipedia.org/w/api.php"
        

    def get_page_id(self, latitude, longitude):
        coordinates = f"{latitude}|{longitude}"
        params = {
            "action" : "query",
            "list" : "geosearch",
            "gsradius" : 10,
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
            "prop" : "info|extracts",
            "inprop" : "url",
            "exsentences" : 5,
            "explaintext" : True,
            "pageids" : pageid
        }

        request = requests.get(self.url, params)
        data = request.json()
        info = data["query"]["pages"][str(pageid)]["extract"]
        url = data["query"]["pages"][str(pageid)]["fullurl"]
        return info, url
        


def run():
    test = Mediawiki()
    test.get_page_id(48.85837009999999, 2.2944813)
    test.extract_info(1359783)

if __name__ == "__main__":
    run()

