import pytest
from parser import Parser

#def hello(name):
#    return "Hello " + name

#def test_hello():
#    assert hello('Fabrice') == "Hello Fabrice"

class Parser_Test:

    def parsing_test_lower(self):
        sentence_test1 = Parser("Place Charles De Gaulles Lille France")
        assert sentence_test1.parsing() == "place charles de gaulles lille france"

    def parsing_test_ponctuation(self):
        sentence_test2 = Parser('Place Charles de Gaulles, Lille, France')
        assert sentence_test2.parsing == "place charles de gaulles lille france"

    