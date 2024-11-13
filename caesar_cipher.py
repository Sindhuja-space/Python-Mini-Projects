import caesar_art

print(caesar_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

def caesar(original_text, shift_amount):
    cipher_text = ""
    if direction == "encode":
        for letter in original_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]

        print(f"Here is the encoded result: {cipher_text}")
    elif direction == "decode":
        for letter in original_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            cipher_text += alphabet[new_position]

        print(f"Here is the decoded result: {cipher_text}")
    else:
        print("Enter a valid input")
  
while should_continue:

    direction = input("Type 'encode' to Encrypt or 'decode' to Decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift)

    user_choice = input("Type 'Yes' to continue or 'No' to exit:\n").lower()
    if user_choice == "no":
        should_continue = False
        print("Good Bye!")
