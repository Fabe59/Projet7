import re
from settings.config import STOPWORDS


class Parser():
    """ Class to parse the sentence indicated by the user """

    def __init__(self, sentence):
        self.sentence = sentence

    def parsing_lowercase(self):
        """ To put all words of the sentence in lowercase """
        self.sentence = self.sentence.lower()
        return self.sentence

    def parsing_ponctuation(self):
        """ To remove all ponctuation from the sentence """
        self.sentence = re.sub(r"[.!,;?:\']", " ", self.sentence)
        return self.sentence

    def split_sentence(self):
        """ To split sentence into a words list """
        self.sentence = self.sentence.split()
        return self.sentence

    def parsing_stopwords(self):
        """ To remove all stopwords from the sentence """
        sentence_ordered = ""
        for word in self.sentence:
            if word not in STOPWORDS:
                sentence_ordered += word + " "
        return sentence_ordered.strip()
