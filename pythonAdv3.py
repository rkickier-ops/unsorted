'''
Ryan and Jerry
Adventure 3
User has to pass the vibe check of the guard to advance in their adventure
Sources: Gemini AI

'''

#Shoutout gemini for the intro this is tuff ugly but functional

secretPassword = "aegis"

def password():

    #Function variable for password attempt
    passAttempt = input("What password would you like to try? (lowercase please)\n")
    attempts = 1

    while passAttempt != secretPassword:
        print(f'{passAttempt} is incorrect, you may not pass until you give the correct password. This is strike {attempts}.')
        passAttempt = input("What password would you like to try? (lowercase please)\n")
        attempts += 1

    print(f'Ah, welcome to Oakhaven. The aegis of Arizona. It only took {attempts} tries!')


    return


def paths(choice):
    if choice == 1:
        print('\n\"Ah, you have chosen Shadowfen Trail. You must be a hardened warrior, best of luck.\"')
    elif choice == 2:
        print("\n\"The Sweet Darling Meadows? You must be a simple shopkeep. Be gone.\"")
    else:
        print("You swing at the guard. He parries, and kills you instantly.")


    return

def main():
    print("The great gates of Oakhaven stand before you, carved from ancient oak and bound in tarnished iron. A guard, a shadow in heavy armor, detaches from the stone wall, their presence a silent and unyielding aegis against the dangers of the world. The air between you is thick with silent judgment as their hand rests on a sheathed blade. \n\n\"Speak the password to advance,\" they say, their voice as unyielding as the stone behind them.")
    password()
    print("Two paths lie before you. Do you continue down path 1 or path 2? ")
    choice = int(input("Path 1 or 2? "))
    paths(choice)
    return

main()
