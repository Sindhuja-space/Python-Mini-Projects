import random

word_list = ["apple", "camel", "blue"]

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()

for letter in guess:
    if letter in chosen_word:
        print("Right")
    else:
        print("Wrong")