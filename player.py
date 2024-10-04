#:::::::::::::::::::::::::::: CARDS -> Player ::::::::::::::::::::::::::::::::#
"""
        The blueprint for the players in the game, namely the PC and the user.
        - Hit -> draws a card, adds it to the player hand, then prints the drawn card.
        - Stand -> If the player choses to stand, this is printed.
        - Is busted -> Checks if the player has more than 21 in hand value.
        - Show hand -> Prints the players hand.

"""
from card import Card
from hand import Hand
from deck import Deck


class Player:
#-----------------------------:: INIT ::----------------------------#
    #We create a bool to deal with the dealer(PC).
    def __init__(self, name: str, is_dealer: bool = False) -> None:
        self.name = name #Players name
        self.hand = Hand() #Calling for Hand() from Hand.py
        self.is_dealer = is_dealer #To differ between dealer(pc) and player

#-----------------------------:: METHOD - Hit ::----------------------------#
    def hit(self, deck: Deck) -> None:
        card = deck.draw_card() #Draws a card from the deck (Method from Deck.py)
        self.hand.add_card(card) #Adds it to the players hand (Method from Hand.py)
        print(f'{self.name} drew: {card.show_card()}') # Presents the drawn card(Method from Card.py)
        self.show_hand() #Shows the hand(Method from Hand.py)

#-----------------------------:: METHOD - Stand::----------------------------#
    def stand(self) -> None:
        print(f'{self.name} stands.') #A simple print, if player choses to stand.

#-----------------------------:: METHOD - Busted ::----------------------------#
    def is_busted(self) -> bool:
        return self.hand.calculate() > 21 #Checks if the players total hand value is more than 21.

#-----------------------------:: METHOD - Show Hand::----------------------------#
    def show_hand(self) -> None:
        print(f'{self.name} hand:')
        self.hand.show_hand() #Shows the hand(Method from Hand.py)