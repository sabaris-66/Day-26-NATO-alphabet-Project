import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
new_data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for index, row in new_data.iterrows()}
#print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
game_is_on = True
while game_is_on:
    user_input = input("enter your name or any other word:").upper()
    try:
        for letter in user_input:
            print(f"{letter} for {new_dict[letter]}")
    except KeyError:
        print("Try to enter only alphabets, Please!")

