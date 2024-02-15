class CardDeck ():

    def __init__(self): 
        self.deck = {"hearts" : self.suite(), "diamonds" : self.suite(), "clubs" : self.suite(), "spades" : self.suite()}
        self.count = 52

    def suite(self):
        return {
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "10": 10,
            "Jack" : 10,
            "Queen" : 10,
            "King" : 10,
            "Ace" : 11,
        }
    
        
    
    def draw_card(self):
        import random 
        suites = ['hearts', "diamonds", "spades", "clubs"]

        suite_name = random.choice(suites)
        suite = self.deck[suite_name]

        if(self.count == 0):
            print("No more cards left")
            pass
        
        try:
            card = random.choice(list(suite.keys()))

            card_value = suite[card]

            del suite[card]
            self.count = self.count - 1

            return {suite_name : {card : card_value}}
        except IndexError:
            self.draw_card()
        
        
    
    def __str__(self):
        return str(self.deck)
    

    
    


class CardHand():

    def __init__(self):
        self.hand = {"hearts" : {}, "diamonds" : {}, "clubs" : {}, "spades" : {}}
        self.total_high = 0
        self.total_low = 0


    def add_card (self, card):

        suite_key = list(card.keys())[0]
        suite_value = list(card.values())[0]
        card_value = list(suite_value.values())[0]
        card_key = list(suite_value.keys())[0]

        if(card_key == 'Ace'):
            self.total_high += 11
            self.total_low += 1
        else:
            self.total_high += card_value
            self.total_low += card_value


        (self.hand[suite_key])[card_key] = card_value

    def total(self):
        if(self.total_high > 21):
            return self.total_low
        else:
            return self.total_high
        

    def __str__(self):
        output = ""

        for key, value in self.hand.items():
            for name, v in value.items():
                output = output + f"{str(name)} of {str(key)}\n"

        return output