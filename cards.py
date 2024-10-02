#---------------------------------:: CARDS -> Class ::------------------------#
class Cards:                                                                       # En klass/BP för all kort
    def __init__(self, cards_suits: list, cards_cards: list, cards_values: list) -> None:   # Kort namn, typ och nr

        #----------------------------:: CARDS ->  ::--------------------------#             #All card types
        self.cards_suits = ['🖤', '❤️', '💠', '⚫'] #⚜💠
        self.cards_cards =['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        deck = []
        for i in range(len(cards_cards)):
            c = cards_cards[i]
            v = cards_values[i]
            for s in cards_suits:
                deck.append((c, s, v))

    def print_deck(self):
        print('Here is all the card combinations and values: \n')
        for card in self.deck:
            print(card)   


#------------------------TESTING AREA------------------------#
if __name__ == "__main__":
    kortlek = Cards()  # Skapa ett kortobjekt
    kortlek.print_deck()  # Visa kortleken