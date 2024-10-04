#:::::::::::::::::::::::::::: CARDS -> Game Engine ::::::::::::::::::::::::::::::::#
"""
        Blueprint for how the game should be played out. Initalizes with deck and player.
        - Play -> Lets each player play out their turn, and end of round checks for winner.
        - Player turn -> As long as they're not busted, asks them for action.
        - Dealer turn -> Dealer shows hand, then draws cards until 17.

"""
from card import Card
from hand import Hand
from deck import Deck
from player import Player


class GameEngine:
#-----------------------------:: INIT ::----------------------------#
    def __init__(self, player_names:list) -> None:
        #Initialize the game with deck and then players accordingly.
        self.deck = Deck() #Creates the deck (Method from Deck.py)
        self.deck.shuffle() #Shuffles the newly created deck (Method from Deck.py)
        self.players = [Player(name) for name in player_names] #Create the players (Method from Player.py)
        self.dealer = Player('Dealer', is_dealer=True) #Create the dealer (PC) (Method from Player.py)
        self.players.append(self.dealer) #appends dealer as last player

#-------------------------:: METHOD - Play loop ::----------------------#
    def play(self) -> None:
        for player in self.players:
            if player.is_dealer:
                self.dealer_turn(player)
            else:
                self.player_turn(player)
        self.check_winner()
#------------------------:: METHOD - Players Turn ::--------------------#
    def player_turn(self, player: Player) -> None:
        while not player.is_busted(): #As long as the player isn't 21+ in hand value
            print(f"\n🃏{player.name}'s turn 🎯")
            player.show_hand() #Shows current hand(Method from Player.py)
            action = input(f'{player.name} 🃏hit or ✋stand? (h/s): ').lower() #Ask player for action

            if action == 'h': #if player choses to hit
                player.hit(self.deck) #Call for hit from Player.py

                if player.is_busted(): #If player is 21+ in hand value (is_busted from Player.py)
                    print(f"💥{player.name} busted with a total of {player.hand.calculate()}!")
                    break

            elif action == 's': #If player choses to stand, nothin happens
                player.stand()
                break
#-------------------------:: METHOD - PC's Turn ::----------------------#       
    def dealer_turn(self, dealer: Player) -> None: 
        print(f"\n🎴Dealer's turn.")
        dealer.show_hand() #Shows dealers currnt hand(Method from Player.py)

        while dealer.hand.calculate() < 17: #As long as the dealer is below 17 in hand value(calculated through calculate from hand.py)
            dealer.hit(self.deck) #The dealer will hit

        if dealer.is_busted(): #When the dealer is busted, print the loss
            print(f"💥 The dealer busted with a total of {dealer.hand.calculate()}!")

        else: #else print dealers current hand value
            print(f'✋The Dealer stands with a total of {dealer.hand.calculate()}')

#----------------------:: METHOD - Check Winner ::--------------------#
    def check_winner(self) -> None: 
        best_score = 0 #The initial value of the best score
        winner = None #Initial winner
        for player in self.players:
            if not player.is_busted(): #If the player is not busted
                player_score = player.hand.calculate() #calculate the players hand value
                if player_score > best_score and player_score <= 21: #If the player has a better score than the best score and is below 21
                    best_score = player_score #The best score is replaced by player
                    winner = player #And the player gets the win
                elif player_score == best_score and winner and winner.is_dealer:
                    winner = self.dealer #If the dealer has the same score as the player, the dealer wins
        if winner: #If it's true that there is a winner, it prints out the winner and the score
            print(f"\n👑{winner.name} wins the game with a total of {best_score}!👑")
        else:
            print(f"\n 💥💥💥No winner, everyone busted!💥💥💥")

#------------------------:: METHOD - ASCII ART :: ------------------------#
    def display_intro(self) -> None:
        print("🎉🎲 VÄLKOMNA TO THE GAME: TJUGOETT!!!! 🎲🎉")
        print("=====================================================")
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        print("⭐     🌟 Get close to 21 without going över! 🌟      ⭐")
        print("⭐        🔥 Vill du beat the dealer? 🔥             ⭐")
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        print("🌟 Aces are worth 1 🌟 | Face cards have unique values! 🎴")
        print("====================================================\n")

        # ASCII Cards Display:
        print("🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂭 🂮 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎")
        print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
        print("🌟 Let’s Begin! 🌟\n")
    
    def game_over_animation(self) -> None:
        print("🎮 Game Över! 🎮")
        for i in range(3):
            print("." * (i + 1), end="\r")
        print("Thanks for playing Tjugoett! ✨👋")