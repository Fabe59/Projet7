from parser import Parser
from googlemaps import GoogleMaps
import urllib.request

class Test_Parser:
    
    def test_parsing_lowercase(self):
        sentence_test1 = Parser("Place Charles de Gaulles Lille France")
        assert sentence_test1.parsing_lowercase() == "place charles de gaulles lille france"

    def test_parsing_ponctuation(self):
        sentence_test2 = Parser("3, Place Charles de Gaulles, Lille; France!")
        assert sentence_test2.parsing_ponctuation() == "3  Place Charles de Gaulles  Lille  France "
    
    def test_split_sentence(self):
        sentence_test3 = Parser("Place Charles de Gaulles")
        assert sentence_test3.split_sentence() == ["Place", "Charles", "de", "Gaulles"]

    def test_parsing_stopwords(self):
        sentence_test4 = Parser([ 'je', 'voudrais', 'aller', 'Place', 'du', 'Trocadero', 'à', 'Paris' ])
        assert sentence_test4.parsing_stopwords() == ['Place', 'Trocadero', 'Paris']
    
class Test_GoogleMaps:

    def test_request_googlemaps(self, monkeypatch):
        request_google_test = GoogleMaps()
        results = {
            "results": [
        {
         "formatted_address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
         "geometry": {
            "location": {
               "lat": 48.85837009999999,
               "lng": 2.2944813
               }
         }}]}
            

        def mockreturn(request):
            return results
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        assert request_google_test.get_coordinates("Tour Eiffel") == (results['results'][0]['formatted_address'], results['results'][0]['geometry']['location']['lat'], results['results'][0]['geometry']['location']['lng'])