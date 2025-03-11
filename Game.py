import random

class Dealer:
    def __init__(self, deck):
        self.deck = deck

    def hand_cards(self):
        random.shuffle(self.deck)
        return self.deck.pop(0)
    
class Player:
    def __init__(self, name, dealer):
        self.name = name
        self.hand = []
        self.dealer = dealer

    def hit(self):
        self.hand.append(self.dealer.hand_cards())
        if 'A' in self.hand:
            value = int(input("Would you like the value of a to be 1 or 11? "))
            if value == 1:
                self.hand.replace('A', 1)
            else:
                self.hand.replace('A', 11)
        return self.hand
    
    # def stand(self):
    #     return self.hand

    
def main():
    letters_dict = {
    'J': 10,
    'Q': 10,
    'K': 10
    }
    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, letters_dict['J'], letters_dict['Q'], letters_dict['K']]
        
    dealer = Dealer(deck)
    name = input("What is your name? ")
    player = Player(name, dealer)
    print(player.hit())



if __name__ == "__main__":
    main()


