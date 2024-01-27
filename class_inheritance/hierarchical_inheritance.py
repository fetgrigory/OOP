'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''
import random


class Question:
    """AI is creating summary for
    """
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display_question(self):
        """AI is creating summary for display_question
        """

        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def check_answer(self, user_input):
        """AI is creating summary for check_answer

        Args:
            user_input ([type]): [description]

        Returns:
            [type]: [description]
        """
        return user_input == str(self.answer)


class Game:
    """AI is creating summary for
    """
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        """AI is creating summary for start
        """
        random.shuffle(self.questions)
        for question in self.questions:
            question.display_question()
            user_input = input("Enter your answer (1-4): ")
            if question.check_answer(user_input):
                self.score += 1
                print("Correct!")
            else:
                print("Wrong!")
        self.end_game()

    def end_game(self):
        """AI is creating summary for end_game
        """
        print(f"Game over! Your final score is {self.score}/{len(self.questions)}")

# Create questions


question1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], 2)
question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Neptune", "Venus"], 1)
question3 = Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], 1)

# Create a game with questions
game = Game([question1, question2, question3])

# Start the game
game.start()
