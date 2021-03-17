import random

class MoralityCore:
    def __init__(self):
        self.sentence_list = ["Why did I need to continue testing. TDD, TDD, TDD everywhere but is it fine to test with people ?"]
        self.sentence_list.append("The purpose of the project ? Hum, well I did not think about it. Let's talk about that next time")
        self.sentence_list.append("Hum, if I add poison on the next room... Nop, bad idea.")
    
    def get_sentence(self):
        choice = random.choice(self.sentence_list)
        print("Current Choice : {0}".format(choice))
        return choice