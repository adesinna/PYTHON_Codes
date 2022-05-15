NAME_HOLDER = "[name]"  # the string we are going to replace

with open("Input/Names/invited_names.txt") as names_file:  # we open up the file folder!
    names = names_file.readlines()  # readline is different from read, read lines() will list the content of the list
    print(names)

with open("Input/Letters/starting_letter.txt") as letter_file:  # we open the letter file needed!
    letter = letter_file.read()  # you want to see what is in the file
    print(letter)

# Next we replace [name] by each name in the list

for name in names:
    stripped_name = name.strip()  # to remove the \n from the names
    new_letter = letter.replace(NAME_HOLDER, stripped_name)  # use the replace method
    print(new_letter)
    # we must keep the letter somewhere
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as complete_letter:
        complete_letter.write(new_letter)  # write new letter in each file
