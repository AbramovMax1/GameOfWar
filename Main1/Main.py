from CardGame1.CardGame import CardGame
import pyfiglet
from colorama import Fore
# =============================================
game_title = pyfiglet.figlet_format("Game Of War", font="doom")
print(Fore.MAGENTA + game_title)
# =============================================
print(Fore.BLUE + "==========♦️♠️♥️♣️============"
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
    print(Fore.RED)
    print(f"ROUND {i}")
    print(Fore.RESET)
    card_p1 = start_game.player1.get_card()
    card_p2 = start_game.player2.get_card()

    print(f"[{player_name_1}] card Pulled --->{card_p1}"
          f" against "
          f"{card_p2}<--- card Pulled [{player_name_2}]")

    if card_p1 > card_p2:
        start_game.player1.add_card(card_p1)
        start_game.player1.add_card(card_p2)
        print(f"{start_game.player1.name} wins this round\n"
              f"[{start_game.player1.name},have {start_game.player1.count_of_cards}] cards\n"
              f"[{start_game.player2.name},have {start_game.player2.count_of_cards}] cards"
              f"\n========♦️♠️♥️♣️========")
    else:
        start_game.player2.add_card(card_p1)
        start_game.player2.add_card(card_p2)
        print(f"{start_game.player2.name} wins this round\n"
              f"[{start_game.player1.name},have {start_game.player1.count_of_cards}] cards\n"
              f"[{start_game.player2.name},have {start_game.player2.count_of_cards}] cards"
              f"\n========♦️♠️♥️♣️========")

# =============================================
print(Fore.GREEN + start_game.get_winner())
# =============================================
print(Fore.BLUE + "\n==========♦️♠️♥️♣️============"
      "\nCREDITS:\n"
      "(Created) by Shirel and Maxim\n"
      "==========♦️♠️♥️♣️============")
# =============================================
