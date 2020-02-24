import re

class Parser():
    """ Class to parse the sentence indicated by the user """
    
    def __init__(self, sentence):
        self.sentence = sentence

    def parsing(self):
        self.sentence = self.sentence.lower()
        self.sentence = re.sub(r"[.!,;?\']", "", self.sentence)
        print(self.sentence)


def test():
    sentence_test = Parser("Place Charles De Gaulles, Lille, France")
    sentence_test.parsing()

if __name__ == "__main__":
    test()
    