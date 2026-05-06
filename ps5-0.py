'''
Ryan Farragher
Problem Set 5
This program makes and uses multiple functions to manipulate strings for password generation
Sources: https://openstax.org/books/introduction-python-programming/pages/8-3-searching-testing-strings Chapter 8
https://www.py4e.com/html3/06-strings Chapter 6
'''



#Tests if a password uses forbidden characters
def test_password(userPass,forbidden='!@$'):
    for x in userPass:
        if x in forbidden:
            return False
    return True

#Takes a string parameter and alters it based on the problems set directions
def make_secret_password(userPass):

    #Variables for the new string
    first = userPass[0]
    last = userPass[-1]
    newPass = last + userPass[1:-1] + first

    #Replacing the designated characters
    newPass = newPass.replace('s','$')
    newPass = newPass.replace('S','$')
    newPass = newPass.replace('A','@')
    newPass = newPass.replace('a','@')

    return newPass

def main():
    print(f'Welcome to the password scrambler, please input a password without !@$ in it')

    userPass = input()

#Loop to ensure user follows directions
    validity = True
    while validity:
        if test_password(userPass):
            validity = False
        else:
            print('Invalid password, forbidden character detected, please try again')
            userPass = input()

    userPass = make_secret_password(userPass)
    print(f'Your new secret password is {userPass} ...shhh don\'t tell anyone')

    return


main()







