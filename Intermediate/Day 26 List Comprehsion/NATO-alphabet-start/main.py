import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')


data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


user_input = input('Enter the name:\n').upper()

new_list = [data_dict[letter] for letter in user_input]

print(new_list)






