import random


class GrandPyMessages:
    """ Class to display a random messagefrom a list of GranPy Bot messages """

    LIST_MESSAGE = [
                    "Et voilà!",
                    "Facile, voici ce que je peux te dire :",
                    "Voilà quelques infos sur le lieu que tu cherches :",
                    "Oh mais je connais bien ce lieu :"
                    ]

    def random_message(self):
        message = random.choice(GrandPyMessages.LIST_MESSAGE)
        return message
