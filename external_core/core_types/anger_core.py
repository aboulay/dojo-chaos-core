import random

class AngerCore:
    def __init__(self):
        self.sentence_list = ["Holy s***! Another test failed. How can they be stupid like this?"]
        self.sentence_list.append("Don't jump on the hole. Here we go again.")
        self.sentence_list.append("I think I need to change my job. Oh yeah, I'm locked here. Grrr")
        self.sentence_list.append("To slow! I'll smash this one on the next test room.")
    
    def get_sentence(self):
        choice = random.choice(self.sentence_list)
        print("Current Choice : {0}".format(choice))
        return choice