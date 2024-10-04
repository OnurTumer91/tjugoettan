#:::::::::::::::::::::::::::: CARDS -> Hand ::::::::::::::::::::::::::::::::#
"""
        The blueprint for the cards that a player holds.
        Add card -> Acts out as a "hit" and adds a card to the hand
        Calculate -> Just reiterates and updates latest value of the hand

"""
from card import Card

class Hand: #Blueprint for the hand of cards
#--------------------:: INIT ::------------------#
    def __init__(self) -> None:
        self.cards: list[Card] = [] # Cards hold in the hand/card objects(list)
        #self.cards is a list of "Card" objects(from card.py)
        self.value = 0 #Initial value of the hand at start of gam

#--------------------:: METHOD - Add Card ::------------------#
    def add_card(self, card: Card) -> None:
        self.cards.append(card) #Adds a card to players hand
        self.value += card.value #Plusses on top the new card to the total hand value
    
#--------------------:: METHOD - Calculate ::------------------#
    def calculate(self) -> int:
        return self.value #Reiterate the calculation of the hand value
    
#--------------------:: METHOD - Show Hand ::------------------#
    def show_hand(self) -> None:
        display_hand = [card.show_card() for card in self.cards] #List all cards in hand
        print(f"Hand: {', '.join(display_hand)}") #A nice print to display the current value
        print(f'Total value: {self.value}') #Another nice way to display; the total value of the hand