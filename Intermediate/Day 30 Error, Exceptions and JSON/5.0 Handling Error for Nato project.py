import pandas as pd  # import pandas

data = pd.read_csv('nato_phonetic_alphabet.csv')  # the data


def code():

    data_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # dictionary comprehension

    user_input = input('Enter the name:\n').upper()
    try:  # the error
        new_list = [data_dict[letter] for letter in user_input]
    except KeyError:  # what it should do
        print('Make sure you enter alphabets')
        code()  # do a recursive
    else:
        print(new_list)


code()
