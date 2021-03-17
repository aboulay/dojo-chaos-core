import random

class IntelligenceCore:
    def __init__(self):
        self.sentence_list = ["If my supposition is fine, showing the cake will increase subject potential... or not. This is extremely strange."]
        self.sentence_list.append("If a fish can fly, the subject could to it too right? Jumping room time!")
        self.sentence_list.append("If my calculations are correct, the subject has just arrived ... not on the platform.")
        self.sentence_list.append("10h, break time. Let's read my new book 'How to test to avoid production accident'.")
    
    def get_sentence(self):
        choice = random.choice(self.sentence_list)
        print("Current Choice : {0}".format(choice))
        return choice