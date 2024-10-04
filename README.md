# Tjugoettan 
Swedish Blackjack game(Tjugoett) made for the following criterias:
* Player draws cards and decides whether to hit or stand
* Ess counted as 1, 
* Player loses if over 21
* Dealer draws until 17 or more
* The winner is determined based on hand value comparisons, and ties go to the dealer.

ULM:
Card 

- suit: str     
- rank: str     
- value: int    
+ show_card()


Deck 

- suits: List
- ranks: List
- deck: List 
+ create_deck()
+ shuffle()   
+ draw_card()
+ print_deck()


Hand     

- cards: List
- value: int 
+ add_card()
+ calculate()
+ show_hand()
  

Player     

- name: str
- is_dealer: bool
+ hit()
+ stand()       
+ is_busted()
+ show_hand

GameEngine

- deck: Deck   
- players: List
+ play()        
+ player_turn()   
+ dealer_turn()    
+ check_winner()
+ display_intro()
+ game_over_animation()

