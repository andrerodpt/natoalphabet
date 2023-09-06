import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_phonetic_alphabet_list = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()

phonetic_translation = [nato_phonetic_alphabet_list[letter] for letter in user_input]

print(phonetic_translation)


