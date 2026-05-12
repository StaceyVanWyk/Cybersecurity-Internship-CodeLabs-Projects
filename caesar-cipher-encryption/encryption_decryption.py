""" This programm will receive the message in plain text then encrypt
     the messagge and then decrypt the message """
"""Simple terms user types in a message the program scramble its and then unscramble it 
   This program teaches me about Core Cybersecurity concepts: Data Confidentiality
   Concept that I am learning IPO Model
Input - user message
Process - encryption logic
Output - encrypted message  """
# Step 1 ask the user for a message 
user_message = input("Please enter your message: ")
#print(user_message)
#if you to store a result initialize a variable with an empty string
result = ""

# Loop through each character
for char in user_message:
    # Preserve spaces and any non-letter characters unchanged
    if char.isupper():
        shifted = (ord(char) - 65 + 3) % 26 + 65
        result += chr(shifted)
    elif char.islower():
        shifted = (ord(char) - 97 + 3) % 26 + 97
        result += chr(shifted)
    else:
        result += char

print(result)