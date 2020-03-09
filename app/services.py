from models.parser import Parser
from models.googlemaps import GoogleMaps
from models.mediawiki import Mediawiki


class Services():

    def __init__(self):
        pass

    def services(self, user_text):
        parser = Parser(user_text)
        sentence_parser = parser.parsing_lowercase()
        sentence_parser = parser.parsing_ponctuation()
        sentence_parser = parser.split_sentence()
        sentence_parser = parser.parsing_stopwords()
        google = GoogleMaps()
        address, lat, long = google.get_coordinates(sentence_parser)
        mediawiki = Mediawiki()
        page_id = mediawiki.get_page_id(lat, long)
        return mediawiki.extract_info(page_id)



       