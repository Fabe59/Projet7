from models.parser import Parser
from models.googlemaps import GoogleMaps
from models.mediawiki import Mediawiki
from models.grandpymessages import GrandPyMessages


class Services():

    def __init__(self):
        pass

    def services(self, user_text):
        message = GrandPyMessages()
        grandpymessage = message.random_message()

        parser = Parser(user_text)
        sentence_parser = parser.parsing_lowercase()
        sentence_parser = parser.parsing_ponctuation()
        sentence_parser = parser.split_sentence()
        sentence_parser = parser.parsing_stopwords()

        google = GoogleMaps()
        address, lat, long = google.get_coordinates(sentence_parser)

        mediawiki = Mediawiki()
        page_id = mediawiki.get_page_id(lat, long)
        extract, url = mediawiki.extract_info(page_id)

        data = {
            "question": sentence_parser,
            "message": grandpymessage,
            "address": address,
            "latitude": lat,
            "longitude": long,
            "info": extract,
            "url": url
        }

        return data
