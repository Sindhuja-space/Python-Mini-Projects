print('''
   ____...------------...____
  _.-"` /o/__ ____ __ __  __ \o\_`"-._
  .'     / /                    \ \     '.
|=====/o/======================\o\=====|
|____/_/________..____..________\_\____|
 /   _/ \_     <_o#\__/#o_>     _/ \_   \
\_________\####/_________/
|===\!/========================\!/===|
|   |=|          .---.         |=|   |
|===|o|=========/     \========|o|===|
|   | |         \() ()/        | |   |
|===|o|======{'-.) A (.-'}=====|o|===|
| __/ \__     '-..-'    __/ \__ |
|==== .'.'^'.'.====|
jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
`""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island. Your mission is to find the treasure!")
user_direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'Right'\n").lower()
if user_direction == "right":
    print("You fell in to a hole.")
    print("GAME OVER!")
elif user_direction == "left":
    print("You have come to a lake. There is an island in the middle of the lake.")
    user_choice = input("Type 'Wait' to wait for a boat or 'Swim' to swim across:\n").lower()
    if user_choice == "swim":
        print("Attacked by trout")
        print("GAME OVER!")
    elif user_choice == "wait":
        door = input("Which door do you want to open? Red, Blue, or Green: \n").lower()
        if door == "red":
            print("Burned by fire. GAME OVER!")
        elif door == "green":
            print("Eaten by beasts. GAME OVER!")
        elif door == "blue":
            print("YOU WIN!")
        else:
            print("GAME OVER!")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")

