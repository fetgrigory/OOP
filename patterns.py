'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''
import random
# Game Class for the game


class Game:
    """AI is creating summary for
    """
    def __init__(self):
        self.choices = ["камень", "ножницы", "бумага"]
# Method of getting computer selection

    def get_computer_choice(self):
        """AI is creating summary for get_computer_choice

        Returns:
            [type]: [description]
        """
        return random.choice(self.choices)

    def get_user_choice(self):
        """AI is creating summary for get_user_choice

        Returns:
            [type]: [description]
        """
        choice = input("Выберите камень, ножницы или бумагу: ")
        while choice not in self.choices:
            print("Неверный выбор. Попробуйте ещё раз.")
            choice = input("Выберите камень, ножницы или бумагу: ")
        return choice
# A method for conducting the game and determining the winner

    def play(self):
        """AI is creating summary for play
        """
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы" and computer_choice == "бумага") or (user_choice == "бумага" and computer_choice == "камень"):
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")

# Allows you to create and manage a single instance of the Game class


class GameManagerSingleton:
    """AI is creating summary for

    Returns:
        [type]: [description]
    """
    instance = None

    @staticmethod
    def get_instance():
        """AI is creating summary for get_instance

        Returns:
            [type]: [description]
        """
        if not GameManagerSingleton.instance:
            GameManagerSingleton.instance = GameManagerSingleton()
        return GameManagerSingleton.instance

    def __init__(self):
        self.game = Game()

    def play_game(self):
        """AI is creating summary for play_game
        """
        self.game.play()

# The Factory pattern for creating an instance of the game


class GameFactory:
    """AI is creating summary for
    """
    def create_game(self):
        """AI is creating summary for create_game

        Returns:
            [type]: [description]
        """
        return GameManagerSingleton.get_instance().play_game()

# Creating a game using patterns


game_factory = GameFactory()
game = game_factory.create_game()
