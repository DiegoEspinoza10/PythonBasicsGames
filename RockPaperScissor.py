from random import randrange

class Bot:
    def __init__(self, number_wins):
        self.number_wins = number_wins
    
    def choose(self):
        my_array = ["Rock", "Paper", "Scissors"]
        number = randrange(0, 3)
        return my_array[number]
        
class Player:
    def __init__(self, number_wins):
        self.number_wins = number_wins
    
    def choose(self):
        my_array = ["Rock", "Paper", "Scissors"]
        ask = input("Choose Rock, Paper, or Scissors: ")
        if ask not in my_array:
            return False
        else:
            return ask
        
class Game:
    def __init__(self, player, bot):
        self.player = player
        self.bot = bot

    def winner(self):
        player_choice = self.player.choose()
        bot_choice = self.bot.choose()

        if player_choice == bot_choice:
            return "Tie"
        
        elif player_choice == "Rock" and bot_choice == "Paper":
            self.bot.number_wins += 1
            return "Bot wins"
        
        elif player_choice == "Rock" and bot_choice == "Scissors":
            self.player.number_wins += 1
            return "You win"
        
        elif player_choice == "Paper" and bot_choice == "Scissors":
            self.bot.number_wins += 1
            return "Bot wins"
        
        elif player_choice == "Paper" and bot_choice == "Rock":
            self.player.number_wins += 1
            return "You win"
        
        elif player_choice == "Scissors" and bot_choice == "Rock":
            self.bot.number_wins += 1
            return "Bot wins"
        
        elif player_choice == "Scissors" and bot_choice == "Paper":
            self.player.number_wins += 1
            return "You win"

bot = Bot(0)
player = Player(0)

ask_continue = True
while ask_continue:
    game = Game(player, bot)
    result = game.winner()
    print(result)
    print(f"Bot wins: {bot.number_wins}")
    print(f"Player wins: {player.number_wins}")
    play_again = input("Do you want to keep playing? Yes or No: ")
    if play_again.lower() != "yes":
        ask_continue = False
    print("Thank you for playing!")