fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.


def make_pie(index):
    try:  # If this place brings an error
        fruit = fruits[index]

    except IndexError:  # fix  the error with except
        print('Fruit Pie')
    else:  # What it should do if it goes well
        print(fruit + " pie")


make_pie(2)
