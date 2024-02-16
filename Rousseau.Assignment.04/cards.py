class Deck ():

    def __init__(self): 
        self.deck:list = []
        for suite in self.suites():
            for card in self.cards():
                self.deck.append(Card(name=card, value=(self.cards())[card], suite=suite))
        self.count = 52

    def cards(self):
        return {
            "1" : [1],
            "2" : [2],
            "3" : [3],
            "4" : [4],
            "5" : [5],
            "6" : [6],
            "7" : [7],
            "8" : [8],
            "9" : [9],
            "10": [10],
            "Jack" : [10],
            "Queen" : [10],
            "King" : [10],
            "Ace" : [1, 11],
        }
    
    def suites(self):
        return ["Hearts", "Diamonds", "Clubs", "Spades"]
    
    def draw_card(self):
        import random 

        

        if(self.count == 0):
            print("No more cards left")
            pass

        return random.choice(self.deck)   
        
    def __str__(self):
        return str(self.deck)
    

class Card():
    def __init__(self, name, value, suite):
        self.name:str = name
        self.value:int = value
        self.suite:str = suite

    def __str__(self):
        return f"{self.name} of {self.suite}"
    


class Hand():

    def __init__(self):
        self.hand = []
        self.total_high = 0
        self.total_low = 0


    def add_card (self, card):

        if(card.name == 'Ace'):
            self.total_high += 11
            self.total_low += 1
        else:
            self.total_high += card.value
            self.total_low += card.value

        self.hand.append(card)

    def total(self):
        if(self.total_high > 21):
            return self.total_low
        else:
            return self.total_high
        

    def __str__(self):
        output = ""

        for card in self.hand:
            output = output + f"{card}\n"

        return output