from models.parser import Parser
from models.googlemaps import GoogleMaps
from models.mediawiki import Mediawiki
from models.grandpymessages import GrandPyMessages


class Test_Parser:

    def test_parsing_lowercase(self):
        sentence_test1 = Parser("Place Charles de Gaulles Lille France")
        assert sentence_test1.parsing_lowercase() ==\
            "place charles de gaulles lille france"

    def test_parsing_ponctuation(self):
        sentence_test2 = Parser("3, Place Charles de Gaulles, Lille; France!")
        assert sentence_test2.parsing_ponctuation() ==\
            "3  Place Charles de Gaulles  Lille  France "

    def test_split_sentence(self):
        sentence_test3 = Parser("Place Charles de Gaulles")
        assert sentence_test3.split_sentence() ==\
            ["Place", "Charles", "de", "Gaulles"]

    def test_parsing_stopwords(self):
        sentence_test4 = Parser([
            'je',
            'voudrais',
            'aller',
            'Place',
            'du', 'Trocadero', 'à', 'Paris'])
        assert sentence_test4.parsing_stopwords() ==\
            'Place Trocadero Paris'


class Test_GoogleMaps:

    def test_request_googlemaps(self, monkeypatch):
        result = {
            "results": [
                        {
                            "formatted_address": "Seattle, WA, USA",
                            "geometry": {
                                "location": {
                                    "lat": 47.6062095,
                                    "lng": -122.3320708
                                }
                            }}]}

        def mock_get(requests, params):

            class JsonResponse:

                def json(self):
                    return result

            return JsonResponse()

        monkeypatch.setattr('requests.get', mock_get)
        request_google_test = GoogleMaps()
        result_test = request_google_test.get_coordinates("Seattle")
        assert result_test == ('Seattle, WA, USA', 47.6062095, -122.3320708)


class Test_Mediawiki:

    def test_get_page_id(self, monkeypatch):
        result = {
            "batchcomplete": "",
            "query": {
                "geosearch": [{
                    "pageid": 1359783,
                    "ns": 0,
                    "title": "Tour Eiffel",
                    "lat": 48.858296,
                    "lon": 2.294479,
                    "dist": 8.2,
                    "primary": ""
                }]}}

        def mock_get(url, params):

            class JsonResponse:

                def json(self):
                    return result

            return JsonResponse()

        monkeypatch.setattr('requests.get', mock_get)
        request_mediawiki = Mediawiki()
        result_test = request_mediawiki.get_page_id(48.858296, 2.294479)
        assert result_test == 1359783

    def test_extract_info(self, monkeypatch):
        result = {
            "query": {
                "pages": {
                    "1359783": {
                        "pageid": 1359783,
                        "title": "Tour Eiffel",
                        "fullurl": "https://fr.wikipedia.org/wiki/Tour_Eiffel",
                        "extract": "La tour Eiffel  est une tour de fer puddlé"
                                   "de 324 mètres de hauteur (avec antennes)"
                                   "située à Paris."
                    }}}}

        def mock_get(url, params):

            class JsonResponse:

                def json(self):
                    return result

            return JsonResponse()

        monkeypatch.setattr('requests.get', mock_get)
        request_mediawiki = Mediawiki()
        result_test = request_mediawiki.extract_info(1359783)
        assert result_test == ("La tour Eiffel  est une tour de fer puddlé"
                               "de 324 mètres de hauteur (avec antennes)"
                               "située à Paris.",
                               "https://fr.wikipedia.org/wiki/Tour_Eiffel")


class Test_Grandpymessages:

    def test_random_message(self):
        message = GrandPyMessages.random_message(self)
        assert message in GrandPyMessages.LIST_MESSAGE
