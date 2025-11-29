# ASCII Art Banner for Caesar Cipher Title
print(r"""         
 _____                              _____ _       _               
/  __ \                            /  __ (_)     | |              
| /  \/ __ _  ___  ___  __ _ _ __  | /  \/_ _ __ | |__   ___ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
| \__/\ (_| |  __/\__ \ (_| | |    | \__/\ | |_) | | | |  __/ |   
 \____/\__,_|\___||___/\__,_|_|     \____/_| .__/|_| |_|\___|_|   
                                           | |                    
                                           |_| 
""")

# Creating an extended alphabet list to handle wrap-around shifts
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

# Define the Caesar Cipher function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""  # Output message to store the result
    if cipher_direction == "decode":
        shift_amount *= -1  # Reverse the shift for decoding
    
    for char in start_text:
        # Only shift letters present in the alphabet list
        if char in alphabet:
            position = alphabet.index(char)  # Find current letter index
            new_position = position + shift_amount  # Calculate new index
            end_text += alphabet[new_position]  # Append shifted letter
        else:
            # If the character is not a letter (space, punctuation), keep it unchanged
            end_text += char

    # Display the result
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Loop for continuing the program until the user stops
should_continue = True
while should_continue:
    # Ask the user for encode/decode choice
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
    
    # Input the message to encode/decode
    text = input("Type your message:\n").lower()
    
    # Input the shift amount
    shift = int(input("Type the shift number:\n"))

    # Ensure shift stays within 0–25 range to avoid redundant rotations
    shift = shift % 26

    # Call the Caesar cipher function with the given inputs
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # Ask if user wants to continue
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")