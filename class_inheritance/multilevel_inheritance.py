'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''
import random


class Dice:
    """AI is creating summary for
    """
    def __init__(self, sides):
        self.sides = sides
# A roll of the dice

    def roll(self):
        """AI is creating summary for roll

        Returns:
            [type]: [description]
        """
        return random.randint(1, self.sides)


class Player:
    """AI is creating summary for
    """
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}"

    def play_turn(self):
        """AI is creating summary for play_turn
        """
        dice = Dice(6)  # Creating a dice with 6 faces
        roll = dice.roll()
        print(f"{self.name} rolled a {roll}")
        self.score += roll


class Game:
    """AI is creating summary for
    """
    def __init__(self, players):
        self.players = players
#  An overridden method for starting the game based on the level

    def play_game(self):
        """AI is creating summary for play_game
        """
        num_turns = 3
        for _ in range(num_turns):
            for player in self.players:
                player.play_turn()

    def print_scores(self):
        """AI is creating summary for print_scores
        """
        for player in self.players:
            print(player)


class MultiLevelGame(Game):
    """AI is creating summary for MultiLevelGame

    Args:
        Game ([type]): [description]
    """
    def __init__(self, players, level):
        super().__init__(players)
        self.level = level

    def play_game(self):
        print(f"Starting level {self.level} game:")
        super().play_game()
        print(f"Level {self.level} game finished!")


# Creating players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Creating an object of the Game class
game = Game([player1, player2])

# Starting the game
game.play_game()

# Withdrawal of the account
game.print_scores()

# # Creating an object of the Multi Level Game class
multi_level_game = MultiLevelGame([player1, player2], 2)

# Launching a multi-level game
multi_level_game.play_game()

# Withdrawal score and level
multi_level_game.print_scores()
