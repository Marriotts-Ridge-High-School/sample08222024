import re

f = open("secret.txt", "r")

secret_message = f.read()

stripped_message = re.sub('[\W_]+', ' ', secret_message, flags=re.UNICODE)

message_array = stripped_message.split()
#print(message_array)

longest = 0
long_words = []
for word in message_array:
    if(len(word) > longest):
        longest = len(word)

for word in message_array:
    if(len(word) == longest):
        long_words.append(word)

print(long_words)

f.close()

alphabet_frequencies = {"a":0,
                         "b":0, 
                         "c":0,
                         "d":0, 
                         "e":0, 
                         "f":0, 
                         "g":0, 
                         "h":0, 
                         "i":0, 
                         "j":0, 
                         "k":0, 
                         "l":0, 
                         "m":0, 
                         "n":0, 
                         "o":0, 
                         "p":0, 
                         "q":0, 
                         "r":0, 
                         "s":0, 
                         "t":0, 
                         "u":0, 
                         "v":0, 
                         "w":0, 
                         "x":0, 
                         "y":0, 
                         "z":0}

for character in secret_message:
    for letter in alphabet_frequencies:
        if character == letter.lower():
            alphabet_frequencies.update({letter: alphabet_frequencies[letter] + 1})

sorted_keys = sorted(alphabet_frequencies.items(), key=lambda x:x[1], reverse = True)
sorted_dict = dict(sorted_keys)
sorted_letters = list(sorted_dict.keys())


for letter in sorted_dict:
    print(letter, ": ", sorted_dict[letter])

decoded_message = ""

# english_frequencies = ["e", "a", "r", "i", "o", "t", "n", "s", "l", "c", "u", "d", "p", "m", "h", "g", "b", "f", "y", "w", "k", "v", "x", "z", "j", "q"]
# #sorted_letters and english_frequencies are now parallel lists
# choice = input(f"Hit enter to replace {} with {}: ", sorted_letters[0], english_frequencies[0])

# #rewrite this part to traverse the String rather than the dict
# for i, character in enumerate(secret_message):
#     if character.isupper():
#         index = sorted_letters.index(character.lower())
#         decoded_message += english_frequencies[index].upper()
#     elif character.islower():
#         index = sorted_letters.index(character)
#         decoded_message += english_frequencies[index]
#     else:
#         decoded_message += character

decoded_message = secret_message
again = "y"
while again == "y":
    print(decoded_message)
    again = input("Would you like to swap letters? (y/n) ")
    if again == "y":
        first = input("Enter the first letter you would like to swap: ").lower()
        second = input("Enter the second letter you would like to swap: ").lower()
        decoded_message = decoded_message.replace(first, "~")
        decoded_message = decoded_message.replace(first.upper(), "`")
        decoded_message = decoded_message.replace(second, first)
        decoded_message = decoded_message.replace(second.upper(), first.upper())
        decoded_message = decoded_message.replace("~", second)
        decoded_message = decoded_message.replace("`", second.upper())
    else:
        print("Here is the final decoded message: ", decoded_message)



