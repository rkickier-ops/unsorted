'''
Ryan Farragher
Problem set 5
Username functions
Sources: https://openstax.org/books/introduction-python-programming/pages/8-3-searching-testing-strings Chapter 8
https://www.py4e.com/html3/06-strings Chapter 6
'''
import random

#Generates a username based on an employee's name
def usernameGen(name):
    names = name.split(' ')

    username = names[0][0].lower() + names[1].lower()
    username = username + str(numberGen())

    return username

#Random number generator
def numberGen(start=100,end=999):
    return random.randint(start,end)

def main():
    print('Please type your name with a space in between\nEx: Steve Smith')
    name = input()

#Loop to ensure user follows directions and inputs a valid response
    validity = True
    while validity:
        if ' ' in name:
            validity = False
        else:
            print('You must separate your first and last name with a space, try again')
            name = input()

    newUser = usernameGen(name)
    print(f'Your new username is {newUser} ')

    return

main()

