'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''
import functools


def limit_attempts(max_attempts):
    """AI is creating summary for limit_attempts

    Args:
        max_attempts ([type]): [description]
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:  # As long as the number of attempts does not exceed the maximum
                attempts += 1  # Increasing the attempt counter
                result = func(*args, **kwargs)  # Calling the original function
                if result:  # If the result of guessing is successful
                    return True  # Return True and end the game
            print("У вас закончились попытки! Вы не смогли отгадать загадку.")
            return False  # If the attempts have ended, we return False
        return wrapper
    return decorator


@limit_attempts(3)  # Limit the number of attempts to solve the riddle to 3
def guess_riddle():
    """AI is creating summary for guess_riddle

    Returns:
        [type]: [description]
    """
    riddle = "загадка: кто ходит сидя?"
    answer = "шахматист"
    user_answer = input(riddle + "\nВаш ответ: ")
    if user_answer.lower() == answer.lower():
        print("Правильно! Вы угадали загадку.")
        return True  # If the answer is correct, we return True
    print("Неправильно! Попробуйте еще раз.")
    return False  # If the answer is incorrect, we return False


guess_riddle()
