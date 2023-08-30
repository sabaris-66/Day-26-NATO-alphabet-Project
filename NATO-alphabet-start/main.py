import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
new_data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for index, row in new_data.iterrows()}
#print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("enter your name or any other word:").upper()
for letter in user_input:
    print(f"{letter} for {new_dict[letter]}")
