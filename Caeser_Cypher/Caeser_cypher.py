from Caeser_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
def ceaser(start_text , shift_amount , cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
            elif cipher_direction == "decode":
                new_position = position - shift_amount
            else:
                print("Invalid Input:")
            end_text += alphabet[new_position]
        else:
            end_text += char
    if cipher_direction == "encode":
            print(f"The encoded text is {end_text}")
    else:
            print(f"The decoded text is {end_text}")
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))




    shift = shift % 26

    ceaser(start_text = text, shift_amount = shift , cipher_direction = direction)

    result = input("Type 'yes' is you want to go again , Otherwise type 'no'.\n")
    if result == "no" or result == "No" or result == "NO":
        should_continue = False
        print("Goodbye!!")
























































# def encrypt(plain_text , shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The Encoded text is {cipher_text}")
        



# def decrypt(cipher_text , shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"Decoded Text is: {plain_text}")

# if direction == "encode":
#     encrypt(plain_text = text , shift_amount = shift)
# elif direction == "decode":
#     decrypt(cipher_text = text , shift_amount = shift)
# else:
#     print("Invalid Input")

