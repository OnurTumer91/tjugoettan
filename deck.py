from card import Card
import random
#:::::::::::::::::::::::::::: DECK -> Class ::::::::::::::::::::::::::::::::#

#----------------------------:: INIT ::-------------------------------#
class Deck: #Every card and their value combo is hardcoded and not adjustable.
    def __init__(self) -> None: 
        self.suits = ['🖤', '❤️', '💠', '⚫'] #⚜💠
        self.ranks =['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        #creates a deck
        self.deck = self.create_deck() 

#--------------------:: METHOD - CREATE DECK::-------------------------#
    def create_deck(self) -> list: #Creating a deck of cards as a list of Card objs
        deck = []
        for i in range(len(self.ranks)): #Iterate all ranks one by one
            rank = self.ranks[i]
            value = self.values[i]
            for suit in self.suits:
                deck.append(Card(suit, rank, value))
        return deck
    
#--------------------:: METHOD - SHUFFLE CARDS ::-----------------------------#
    def shuffle(self) -> None:
        random.shuffle(self.deck)

#-----------------------:: METHOD - DRAW CARDS ::-----------------------------#
    def draw_card(self):
        if not self.cards:
            raise Exception("Out of cards: deck empty!")
        card = self.cards.pop()
        return card


#--------------------:: METHOD - PRINT DECK::-----------------------------#
    def print_deck(self) -> None:
        print('Here is all the card combos together with resp. values: \n')
        for card in self.deck:
            print(card.show_card())
