import pytest
from parser import Parser

#def hello(name):
#    return "Hello " + name

#def test_hello():
#    assert hello('Fabrice') == "Hello Fabrice"

class Parser_Test:

    def parsing_test(self):
        sentence_test = Parser("Place Charles De Gaulles Lille France")
        assert sentence_test.parsing() == "place charles de gaulles lille france"