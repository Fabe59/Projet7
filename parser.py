import re
from config import STOPWORDS

class Parser():
    """ Class to parse the sentence indicated by the user """
    
    def __init__(self, sentence):
        self.sentence = sentence

    def parsing(self):
        # To put all words of the sentence in lowercase
        self.sentence = self.sentence.lower()
        # To remove all ponctuation from the sentence
        self.sentence = re.sub(r"[.!,;?:\']", " ", self.sentence)
        # To split sentence into a words list
        self.sentence = self.sentence.split()
        # To remove all stopwords from the sentence
        sentence_ordered = []
        for word in self.sentence:
            if word not in STOPWORDS:
                sentence_ordered.append(word)
        #print(sentence_ordered)


#def test():
#    sentence_test = Parser("Bonjour Grandpy, je recherche l'adresse : 3 Place de l'étoile, Lille; France!")
#    sentence_test.parsing()

#if __name__ == "__main__":
#    test()
    