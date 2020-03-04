from parser import Parser
from googlemaps import GoogleMaps
from mediawiki import Mediawiki


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
        result = {
            "results": [
        {
         "formatted_address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
         "geometry": {
            "location": {
               "lat": 48.85837009999999,
               "lng": 2.2944813
               }
         }}]}
         
        def mock_get(requests, params):

            class JsonResponse:

                def json(self):
                    return result
            
            return JsonResponse()

        monkeypatch.setattr('requests.get', mock_get)
        request_google_test = GoogleMaps()
        result_test = request_google_test.get_coordinates("Tour Eiffel")
        assert result_test == ('Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France', 48.85837009999999, 2.2944813)

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
                        "extract": "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », ce monument est devenu le symbole de la capitale française, et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale Notre-Dame de Paris était en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés mais il reste le monument payant le plus visité au monde,. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs.\nD’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans."
            }}}}

        def mock_get(url, params):

            class JsonResponse:

                def json(self):
                    return result
            
            return JsonResponse()

        monkeypatch.setattr('requests.get', mock_get)
        request_mediawiki = Mediawiki()
        result_test = request_mediawiki.extract_info(1359783)
        assert result_test == ("La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France. Construite par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », ce monument est devenu le symbole de la capitale française, et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 6,9 millions de visiteurs, en 2011 la cathédrale Notre-Dame de Paris était en tête des monuments à l'accès libre avec 13,6 millions de visiteurs estimés mais il reste le monument payant le plus visité au monde,. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs.\nD’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans.", "https://fr.wikipedia.org/wiki/Tour_Eiffel" )
