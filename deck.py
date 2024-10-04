#:::::::::::::::::::::::::::: DECK -> Class ::::::::::::::::::::::::::::::::#
"""
        I create a complete deck of cards from my blueprint of a single card 
        with me new blueprint for a whole deck.
       
        - Create deck -> Creates my set of cards
        - Shuffle -> uses the random module to shuffle the deck
        - Draw card -> deletes the last card from the deck
"""
from card import Card
import random

#----------------------------:: INIT ::-------------------------------#
class Deck: #Every card and their value combo is hardcoded and not adjustable. BP for a deck of cards
    def __init__(self) -> None: 
        self.suits = ['🖤', '❤️', '💠', '⚫'] # May use these instead ⚜💠
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        #Creates a deck
        self.deck = self.create_deck() 

#--------------------:: METHOD - CREATE DECK::-------------------------#
    def create_deck(self) -> list:
        deck = []
        for rank in self.ranks:  # Iterates over all ranks one by one in a loop
            for suit in self.suits:  # for every color(suits) in the deck
                deck.append(Card(suit, rank))  # and creates the card then appends it to the deck
        return deck

    
#--------------------:: METHOD - SHUFFLE CARDS ::-----------------------------#
    def shuffle(self) -> None:
        random.shuffle(self.deck)

#-----------------------:: METHOD - DRAW CARDS ::-----------------------------#
    def draw_card(self) -> Card:
        if not self.deck:
            raise Exception("Out of cards: deck empty!")
        card = self.deck.pop()
        return card


#--------------------:: METHOD - PRINT DECK::-----------------------------#
    def print_deck(self) -> None:
        print('Here is all the card combos together with resp. values:')
        for card in self.deck:
            print(card.show_card())
            

#------------------------TESTING AREA------------------------#
if __name__ == "__main__":
    deck = Deck() #Create a deck of cards
    deck.print_deck()  #Print the newly created deck of cards