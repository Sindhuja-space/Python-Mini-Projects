import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

print("Welcome to the PyPassword Generator!")

n_letters = int(input("How many letters do you want?\n"))
n_numbers =  int(input("How many numbers do you want?\n"))
n_symbols = int(input("How many symbols do you want?\n"))

for char in range(0, n_letters):
    password.append(random.choice(letters))

for char in range(0, n_numbers):
    password.append(random.choice(numbers))

for char in range(0, n_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

password_string = ""

for char in password:
    password_string += char

print(f"Your Password is: {password_string}")