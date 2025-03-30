import random


class Dice:

    def __init__(self):
        self.value = None

    def roll(self):
        new_value = random.randint(1, 6)
        self.value = new_value
        return new_value


class Player:

    def __init__(self, dice, is_player):
        self.dice = dice
        self.is_player = is_player
        self.counter = 10

    def increment(self):
        self.counter += 1
    
    def decrement(self):
        self.counter -= 1
    
    def roll_dice(self):
        return self.dice.roll()


class DiceGame:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start_game(self):
        self.print_welcome()
        while True:
            self.start_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def start_round(self):
        self.new_round()
        
        player_roll = self.player.roll_dice()
        computer_roll = self.computer.roll_dice()

        self.show_rolls(player_roll, computer_roll)
        
        if player_roll > computer_roll:
            print('You won this round! 🎉')
            self.update_counters(winner=self.player, loser=self.computer)
        elif player_roll < computer_roll:
            print('The computer won this round. 😥 Try again.')
            self.update_counters(winner=self.computer, loser=self.player)
        elif self.player.dice.value == self.computer.dice.value:
            print('Its a tie!!')

        self.show_counters()
    
    def print_welcome(self):
        print('🎲 Welcome to Roll the Dice!')

    def new_round(self):
        print('\n------ New Round ------')
        input('🎲 Press any key to roll the dice.🎲 ')

    def show_rolls(self, player, computer):
        print(f'Playered Rolled: {player}')
        print(f'Computered Rolled: {computer}')

    def update_counters(self, winner, loser):
        winner.decrement()
        loser.increment()
    
    def show_counters(self):
        print(f'\nYour counter: {self.player.counter}')
        print(f'Computer counter: {self.computer.counter}')
    
    def check_game_over(self):
        if self.player.counter == 0:
            self.show_game_over(winner=self.player)
            return True
        elif self.computer.counter == 0:
            self.show_game_over(winner=self.computer)
            return True
        else:
            return False
        
    def show_game_over(self, winner):
        if  not winner.is_player:
            print("\n=======================")
            print(" G A M E   O V E R ✨")
            print("The computer won the game. Sorry...")
        else:
            print("\n=====================")
            print(" G A M E   O V E R ✨")
            print("You won the game! Congratulations")


dice1 = Dice()
dice2 = Dice()

user = Player(dice1, True)
computer = Player(dice2, False)

game = DiceGame(user, computer)
game.start_game()
