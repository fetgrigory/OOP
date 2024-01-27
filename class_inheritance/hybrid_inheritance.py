'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''


class Player:
    """AI is creating summary for
    """
    def __init__(self, name):
        self.name = name


class HangmanGame:
    """AI is creating summary for
    """
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []

    def display_word(self):
        """AI is creating summary for display_word

        Returns:
            [type]: [description]
        """
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.rstrip()

    def guess_letter(self, letter):
        """AI is creating summary for guess_letter

        Args:
            letter ([type]): [description]
        """
        self.guessed_letters.append(letter)

    def check_win(self):
        """AI is creating summary for check_win

        Returns:
            [type]: [description]
        """
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True


class Game(HangmanGame, Player):
    """AI is creating summary for Game

    Args:
        HangmanGame ([type]): [description]
        Player ([type]): [description]
    """
    def __init__(self, word, name):
        HangmanGame.__init__(self, word)
        Player.__init__(self, name)

    def start_game(self):
        """AI is creating summary for start_game
        """
        while not self.check_win():
            print("Which programming language uses the .py file extension?")
            print("Word:", self.display_word())
            guessed_letter = input("Guess a letter: ")
            self.guess_letter(guessed_letter)

        print("Congratulations, you won!")
        print("Player name:", self.name)
        print("Guessed word:", self.word)


# Example usage of the game
game = Game("python", "Gregory")
game.start_game()
