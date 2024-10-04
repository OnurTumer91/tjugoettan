#:::::::::::::::::::::::::::: Player -> Class ::::::::::::::::::::::::::::::::#

#----------------------------:: INIT ::-------------------------------#
class Deck: #Every card and their value combo is hardcoded and not adjustable.
    def __init__(self, name: str, budget: int, hand: str) -> None: 
        self.name = name
        self.budget = budget
        self.hand = hand

        #creates a deck
        self.deck = self.create_deck() 

#--------------------:: METHOD - CREATE DECK::-------------------------#
    def hit(self) -> list: #Creating a deck of cards as a list of Card objs


#--------------------:: METHOD - PRINT DECK::-----------------------------#
    def stand(self) -> None:

