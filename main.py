#main.py
#Huvudprogram
from card import Card
from deck import Deck
import random

def shuffle_test():
    #Shuffle Test--------------------------------
    deck = Deck() #Create a deck of cards
    print('----------------Before Shuffle------------------')
    deck.print_deck()  #Print the newly created deck of cards
    deck.shuffle()
    print('----------------After Shuffle------------------')
    deck.print_deck()  #Print the shuffled cards
    #Shuffle Test-----------------------------------

def hand_test():
    deck = Deck()
    deck.shuffle()
    c1 = deck.draw_card()
    c2 = deck.draw_card()
    c3 = deck.draw_card()
    h = Hand([c1, c2,  c3])
    c4 = deck.draw_card()
    h.add(c4)
    print ({h})
    print ({h.value()})


def main() -> None:
    print('Welcome to Blackjack, Swedish style!')

#--------------GAME LOOP-----------#




if __name__ == "__main__":
    main()
    # shuffle_test()
    hand_test()




    ''' Spela mot dator med keyboard input
    -Om spelaren får över 21 förlorar den spelet och datorn vinner
    -Om spelaren stannar under 21, får datorn dra 1 kort i taget och välja om den ska fortsätta eller ej
    -Om datorn får mer än 21 eller mindre  än användaren så vinner användaren, annars datorns vinst.
    -Datorn vinner alltsp på samma poäng
    -((Användaren får välja om ESS räknas som 1 eller 14, OM MAN VILL))
    -((Tillägsregel om 2 eller 3 ess utan andra kort får räknas som 21))

    -Dokumentera arbetet i dina filer (skriv tydliga kommentarer i källkoden).
    -Du visar förståelse för olika datatyper genom typning av variabler och funktioners argument- och returtyper
    -Du visar förstålse för objektorienterad programmering.
    -Använd minst en klass, flera objekt och minst 2 metoder.
    -Ladda upp inlämningsuppgiften till GitHub.
    -Lämna in en länk till GitHub-Repot.
    '''
