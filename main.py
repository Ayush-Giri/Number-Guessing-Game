import random

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")

random_number = random.randint(1, 100)

easy_level_attempts = 10
hard_level_attempts = 5

difficulty_level = input("choose a difficulty level 'easy' or 'hard': ").lower()


def easy(user_number):
    global easy_level_attempts
    if user_number < random_number:
        easy_level_attempts -= 1
        return easy_level_attempts
    elif user_number > random_number:
        easy_level_attempts -= 1
        return easy_level_attempts
    else:
        return None


def hard(user_number):
    global hard_level_attempts
    if user_number < random_number:
        hard_level_attempts -= 1
        return hard_level_attempts
    elif user_number > random_number:
        hard_level_attempts -= 1
        return hard_level_attempts
    else:
        return None


easy_flag = True
hard_flag = True

if difficulty_level == "easy":
    while easy_flag:
        user_guess = int(input(f"you have {easy_level_attempts} attempts remaining guess the number: "))
        easy_function_output = easy(user_guess)
        if easy_function_output is None:
            print("Congratulation you won the game")
            easy_flag = False
        elif easy_function_output == 0:
            print("You lost the game")
            easy_flag = False
        elif user_guess < random_number and easy_function_output > 0:
            print("Sorry the number is low")
        elif user_guess > random_number and easy_function_output > 0:
            print("Sorry the number is high")


elif difficulty_level == "hard":
    while hard_flag:
        user_guess = int(input(f"you have {hard_level_attempts} attempts remaining guess the number: "))
        hard_function_output = hard(user_guess)
        if hard_function_output is None:
            print("Congratulations you won the game")
            hard_flag = False
        elif hard_function_output == 0:
            print("you lost the game")
            hard_flag = False
        elif user_guess < random_number and hard_function_output > 0:
            print("sorry the number is low")
        elif user_guess > random_number and hard_function_output > 0:
            print("sorry the number is high")















