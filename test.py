import pytest
from parser import Parser


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
    