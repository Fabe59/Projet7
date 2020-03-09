from parser import Parser
from googlemaps import GoogleMaps
from mediawiki import Mediawiki


class Services():

    def __init__(self):
        pass

    def services(self, user_text):
        parser = Parser(user_text)
        parser.parsing_lowercase()
        parser.parsing_ponctuation()
        parser.split_sentence()
        return parser.parsing_stopwords()