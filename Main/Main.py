from CardGame.CardGame import CardGame
import pyfiglet
from colorama import Fore
# =============================================
game_title = pyfiglet.figlet_format("Game Of War", font="doom")
print(Fore.LIGHTGREEN_EX + game_title)
# =============================================
print(Fore.YELLOW + "==========♦️♠️♥️♣️============"
      "\nWelcome to Game Of War\nHere you will fight against one opponent\nEvery player gets 26 cards."
      "\nEvery player will throw one card and who get the higher card takes those 2 cards"
      "\nThe player who have less cards then his opponent after 10 rounds loss,"
      "\nAnd the player who have more cards then the opponent win!\nGood Luck and Have Fun"
      "\n==========♦️♠️♥️♣️============")
print(Fore.RESET)
# =============================================
player_name_1 = input("Enter Player1 name :").strip()
amount_cards_1 = 26
player_name_2 = input("Enter Player2 name :").strip()
amount_cards_2 = 26

# =============================================
start_game = CardGame(player_name_1, player_name_2, amount_cards_1, amount_cards_2)
print(start_game)
# =============================================
print("\n==========♦️♠️♥️♣️============")
for i in range(1, 11):
    print(f"ROUND {i}")
    card_p1 = start_game.player1.get_card()
    card_p2 = start_game.player2.get_card()

    print(f"[{player_name_1}] have {start_game.player1.count_of_cards} cards Pulled --->{card_p1}"
          f" against "
          f"{card_p2}<--- [{player_name_2}] Have {start_game.player2.count_of_cards} cards")

    if card_p1 > card_p2:
        start_game.player1.add_card(card_p1)
        start_game.player1.add_card(card_p2)
        print(f"{start_game.player1.name} wins this round\n=======+♦️♠️♥️♣️========")
    else:
        start_game.player2.add_card(card_p1)
        start_game.player2.add_card(card_p2)
        print(f"{start_game.player2.name} wins this round\n========♦️♠️♥️♣️========")

# =============================================
print(Fore.GREEN + start_game.get_winner())
# =============================================
print(Fore.LIGHTYELLOW_EX + "==========♦️♠️♥️♣️============"
      "\nCREDITS:\n"
      "(Created) by Shirel and Maxim\n"
      "(Welcome message) by Gil Andreyev\n==========♦️♠️♥️♣️============")
# =============================================
