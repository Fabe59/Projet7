import re
from config import STOPWORDS

class Parser():
    """ Class to parse the sentence indicated by the user """
    
    def __init__(self, sentence):
        self.sentence = sentence

    def parsing(self):
        self.sentence = self.sentence.lower()
        self.sentence = re.sub(r"[.!,;?:\']", " ", self.sentence)
        self.sentence = self.sentence.split()
        for word in self.sentence:
            if word in STOPWORDS:
                self.sentence.remove(word)
        print(self.sentence)


def test():
    sentence_test = Parser("Bonjour, je veux aller au 3 Place de l'étoile, Lille; France!")
    sentence_test.parsing()

if __name__ == "__main__":
    test()
    