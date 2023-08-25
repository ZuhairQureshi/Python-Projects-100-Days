import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

alpha_frame = pd.read_csv('nato_phonetic_alphabet.csv')

alpha_dict = {row.letter:row.code for (index, row) in alpha_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def encode_word():
    word = input("Enter a word: ").upper()

    try:
        code_words = [alpha_dict[letter] for letter in word]

    except KeyError:
        print("Only alphabets as characters please!")
        encode_word()   # if characters not within alpha_dict are present, re-prompt

    else:
        print(code_words)


encode_word()
