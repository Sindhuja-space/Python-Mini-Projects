import random

word_list = ["apple", "camel", "blue"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for word in range(word_length):
    placeholder += "-"
print(placeholder)

is_game_over = False
correct_letters = []

while not is_game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        is_game_over = True
        print("You Won!")