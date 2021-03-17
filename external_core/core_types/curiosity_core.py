import random

class CuriosityCore:
    def __init__(self):
        self.sentence_list = ["Lets try to add more poison here..."]
        self.sentence_list.append("If I follow the Johnson pattern, perhaps I should find something.")
        self.sentence_list.append("Oh, a test room that I did not test before ! I deploy and... oh too bad, the subject die...")
        self.sentence_list.append("What append if I add more turrets here?")
    
    def get_sentence(self):
        choice = random.choice(self.sentence_list)
        print("Current Choice : {0}".format(choice))
        return choice