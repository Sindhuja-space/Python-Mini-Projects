import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between between 1 and 100")

answer = random.randrange(1, 101)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempts = 10
def set_difficulty(difficulty_level):
    if difficulty_level == "easy":
        print(f"You have {attempts} attempts remaining to guess the number.")   
    elif difficulty_level == "hard":
        print(f"You have {attempts - 5} attempts remaining to guess the number.")

set_difficulty(difficulty_level)

number = input("Make a Guess: ")
