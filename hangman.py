import random
from hangman_words import word_list
from hangman_decorators import logo, stages

print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for word in range(word_length):
    placeholder += "_"
print("Word to guess:" + placeholder)

is_game_over = False
correct_letters = []

while not is_game_over:
    print(f"******** YOU HAVE {lives}/6 LIVES LEFT ********")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed the word {guess}")

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

    if guess not in chosen_word:
      lives -= 1
      print(f"You guessed {guess}, that is not in the word, You lose a life")
      if lives == 0:
        is_game_over = True
        print(f"It was {chosen_word}")
        print("********** GAME OVER, You lose **********")
        

    if "_" not in display:
        is_game_over = True
        print("********** You Won! **********")

    print(stages[lives])