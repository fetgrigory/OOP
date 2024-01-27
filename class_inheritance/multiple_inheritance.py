'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''
import random


class Board:
    """AI is creating summary for
    """
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        """AI is creating summary for print_board
        """
        print('-------------')
        for i in range(3):
            row = '| ' + ' | '.join(self.board[i*3:(i+1)*3]) + ' |'
            print(row)
            print('-------------')

    def is_board_full(self):
        """AI is creating summary for is_board_full

        Returns:
            [type]: [description]
        """
        return ' ' not in self.board

    def is_winner(self, symbol):
        """AI is creating summary for is_winner

        Args:
            symbol ([type]): [description]

        Returns:
            [type]: [description]
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal combinations
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical combinations
            [0, 4, 8], [2, 4, 6]  # Diagonal combinations
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == symbol:
                return True
        return False


class Player:
    """AI is creating summary for
    """
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, game):
        """AI is creating summary for make_move

        Args:
            game ([type]): [description]
        """
        while True:
            # Entering the cell position
            position = input("Enter the cell number (from 1 to 9): ")
            # Converting a position to an integer and subtracting 1 to get the index of a cell in the list
            position = int(position) - 1
            # Check if the selected cell is occupied. If not, then set the player symbol
            if game.board[position] == ' ':
                game.board[position] = self.symbol
                break
            else:
                # Displays an error message if the selected cell is already occupied
                print("The selected cell is already occupied. Try again.")


class AI:
    """AI is creating summary for
    """
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, game):
        """AI is creating summary for make_move

        Args:
            game ([type]): [description]
        """
        # Getting available moves
        available_moves = [i for i, cell in enumerate(game.board) if cell == ' ']
        # Choosing a random position from the available moves
        position = random.choice(available_moves)
        # Setting the AI symbol in the selected position of the game board
        game.board[position] = self.symbol

# Definition of the TicTacToe class, based on the Board, Player, AI.


class TicTacToe(Board, Player, AI):

    """AI is creating summary for TicTacToe

    Args:
        Board ([type]): [description]
        Player ([type]): [description]
        AI ([type]): [description]
    """
    def __init__(self):
        super().__init__()  # Calling the constructor of the parent class
        self.current_player = None  # Initialize the current player

    def play(self):
        """AI is creating summary for play
        """
        self.current_player = Player("X")  # Start with the player who plays for X

        while True:
            self.print_board()  # Bringing out the game board

            print(f"A player walks {self.current_player.symbol}")
            self.current_player.make_move(self)

            if self.is_winner(self.current_player.symbol):
                self.print_board()
                print(f"Player {self.current_player.symbol} victory!")
                break

            if self.is_board_full():  # Check if the game board is full
                self.print_board()
                print("Draw!")
                break

            if isinstance(self.current_player, Player):  # If the current player is an instance of the Player class
                self.current_player = AI("O")  # The current player is an instance of the AI class playing for O
            else:
                self.current_player = Player("X")  # Otherwise, the current player becomes an instance of the Player class playing for X


game = TicTacToe()
game.play()
