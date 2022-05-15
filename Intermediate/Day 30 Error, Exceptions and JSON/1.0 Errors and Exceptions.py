# Errors are meant to happen, but provisions are made for these scenarios!
# Catching exceptions with  Try Except Else Finally 'TEEF'

# FileNotFound Error, suppose you want to open a file that does not exist.

try:
    file = open('a_file.txt')
    a_dictionary = {'key': 1}
    print(a_dictionary['key'])


except FileNotFoundError:  # Each except for different scenarios
    file = open('a_file.txt', 'w')
    file.write('We made this file and wrote this inside')

except KeyError as error_message:
    print(f'The key {error_message} does not exist')

else:  # If it manages to fix the error, it will run the else block!
    content = file.read()
    print(content)

finally:  # It will run no matter what happens
    file.close()  # you can also raise your own exception in finally
    print('File was closed')



