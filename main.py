#:::::::::::::::::::::::::::: Main  ::::::::::::::::::::::::::::::::#
''' 
    Spela mot dator med keyboard input
    -Om spelaren får över 21 förlorar den spelet och datorn vinner
    -Om spelaren stannar under 21, får datorn dra 1 kort i taget och välja om den ska fortsätta eller ej
    -Om datorn får mer än 21 eller mindre  än användaren så vinner användaren, annars datorns vinst.
    -Datorn vinner alltså på samma poäng
'''

from card import Card
from hand import Hand
from deck import Deck
from player import Player
from game_engine import GameEngine
import random

def main():
    game = GameEngine([]) #Iniialize class
    game.display_intro() #Fancy introduciton

    print("🎮 How many players at the table? 🎯" ) #Exclusing the dealer
    num_players = int(input("Number of players: "))
    
    player_names = [] #Register player names
    for i in range(num_players):
        name = input(f"Enter player {i + 1} name: ")
        player_names.append(name)

    game = GameEngine(player_names) #Initialize the game with the player names
    game.play() #Start the game

    game.game_over_animation() #Ending Ascii fanciness


if __name__ == "__main__": #Main
    main()