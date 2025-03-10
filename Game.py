import random


class Dealer:
    def __init__(self, deck):
        self.deck = deck

    def hand_cards(self):
        random.shuffle(self.deck)
        return self.deck.pop(0)
    
def main():
    letters_dict = {
    'J': 10,
    'Q': 10,
    'K': 10
    }

    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, letters_dict['J'], letters_dict['Q'], letters_dict['K']]

        
    dealer = Dealer(deck)
    my_hand = dealer.hand_cards()

    if my_hand == 'A':
        a_value = int(input("Would you like the value of a to be 1 or 11? "))
        if a_value == 1:
            my_hand = 1
        else:
            my_hand = 11

if __name__ == "__main__":
    main()


