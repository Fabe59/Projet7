import pytest
from parser import Parser


def parsing_test(self):
    sentence_test = Parser("Place Charles De Gaulles Lille France")
    assert sentence_test.parsing() == "place charles de gaulles lille france"