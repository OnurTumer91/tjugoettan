#:::::::::::::::::::::::::::: CARDS -> Class ::::::::::::::::::::::::::::::::#

class Card: # En klass/BP för alla kort
    #--------------------:: INIT ::------------------#
    def __init__(self, suit: str, rank: str, value: int) -> None:
        self.suit = suit #['🖤', '❤️', '💠', '⚫'] #⚜💠
        self.rank = rank #['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.value = value #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#--------------------:: METHOD - SHOW CARDS::------------------#
    def show_card(self) -> str:
           #The presentation format of the cards f.eg  Q❤️10
           return f'{self.rank}{self.suit} (Value: {self.value})'
    

#------------------------TESTING AREA------------------------#
# if __name__ == "__main__":
#     deck = Deck() #Create a deck of cards
#     deck.print_deck()  #Print the newly created deck of cards