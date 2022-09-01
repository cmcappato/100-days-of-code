import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

# Take the NATO csv file and:
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word: ").upper()
input_list_of_characters = []

for letter in user_word:
    input_list_of_characters.append(letter)

# print(input_list_of_characters)
output_list_of_nato_alphabet = []

for letter in input_list_of_characters:  # Loop through list of character made of what the user inputs
    for (key, value) in nato_dict.items():  # Loop through the dictionary
        if letter == key:  # When the letter and the key of the dictionary are the same I extract the value and append it to the list
            output_list_of_nato_alphabet.append(value)

print(output_list_of_nato_alphabet)
