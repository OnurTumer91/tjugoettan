#:::::::::::::::::::::::::::: CARDS -> Class ::::::::::::::::::::::::::::::::#
"""
        The blueprint for a single card is made in this calss.       
        - Custom Value -> Assigns custom values for special cards accordingly for Tjugoettan
        - Show Card -> Shows the card in a readable format.

"""
class Card: # BP for a single card
    #--------------------:: INIT ::------------------#
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit # F.eg ❤️
        self.rank = rank # F.eg Q
        self.value = self.custom_value() # Custom assignment so Deck.py can be used in other games.
        #Funny note: I forgot to add the "()" after custom_value and spent a god hour wondering why this wasn't working.
        #Turned out I needed to call the method custom_value, not just refer to it...

    def custom_value(self) -> int:
        if self.rank == 'A':
            return 1  # In Tjugoettan, A is either 1 or 14, I chose 1
        elif self.rank == 'K':
            return 13
        elif self.rank == 'Q':
            return 12 
        elif self.rank == 'J':
            return 11 
        else:
            return int(self.rank)

#--------------------:: METHOD - SHOW CARDS::------------------#
    def show_card(self) -> str:
           #The presentation format of the cards f.eg  Q❤️10
        return f'{self.rank}{self.suit} (värde: {self.value})'


#------------------------TESTING AREA------------------------#
# if __name__ == "__main__":
#     card = Card('❤️', 'Q', 10) #Crate a single card
#     print(card.show_card()) 