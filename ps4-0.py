'''Ryan Farragher
Problem Set 4 Restaurant functions
This program uses a variety of functions to handle some basic restaurant transactions
Will definitely break if the user inputs anything other than numbers
Sources: https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python (Top Answer)
 Chapter 6 of the book
'''

#This Function displays all available functions and runs whatever the user needs
def menu():

    #Validity Variable and loop
    fakeFunc = True
    while fakeFunc:
        print(f'Available functions:\n1:Make Change\n2:Calculate Tip\n3:Cash Out Meal')
        func = int(input('What function do you need?\n'))
        if func >=1 and func <=3:
            fakeFunc = False
        else:
            print('Please input a valid function')

    #If statements to run the correct functions based on user input
    if func == 1:
        #Sets up and runs the function for making change
        bill = float(input('How much was the bill?\n'))
        paid = float(input('How much money did they give you?\n'))
        change = myFuncs[func-1](bill,paid)

        #Validity check
        if paid > bill:
            change = round(change,2)
            print(f'The customer needs ${change} back as change.')


    elif func == 2:
        #Sets up and runs the tip function
        bill = float(input('How much was the bill?\n'))
        tip_percent = float(input('What percentage are they tipping?\n'))

        tip_amt = myFuncs[func-1](bill,tip_percent)
        tip_amt = round(tip_amt,2)

        print(f'The tip at {tip_percent}% is ${tip_amt}')

    else:
        #Sets up and runs the cash out function
        bill = float(input('How much was the bill?\n'))
        tip_percent = float(input('What percentage are they tipping?\n'))
        paid = float(input('How much money did they give you?\n'))

        myFuncs[func-1](bill,tip_percent,paid)




#Makes Change
def make_change(cost,payment):
    #Test if rest needs to run
    if payment < cost:
        print('Insufficient funds!')
        return

    #Returns the change
    return payment - cost


#Calculates and returns the tip
def calc_tip(cost,percent):

    return cost * (percent/100)



#Calculates the full transaction based on given parameters
def cash_out_meal(cost,percent,payment):

    #Checking to see if rest of code should be run
    if payment < cost:
        print('Insufficient funds!')
        return

    #Creates and defines new variables for local use and calls other functions for efficiency
    tip = myFuncs[1](cost,percent)
    tip = round(tip,2)

    bill = cost + tip
    bill = round(bill,2)

    #Secondary Validity check
    if bill < payment:
        change = myFuncs[0](bill,payment)
        change = round(change,2)
    else:
        print('Insufficent Funds!')
        return

    #Prints a formatted ouput and returns nothing
    print(f'Tip amount:${tip}\nTotal bill with tip:${bill}\nAmount paid:${payment}\nChange due:${change}')
    return

myFuncs = (make_change,calc_tip,cash_out_meal)


#Main function for running the program
def main():
    validity = True
    while validity:

        menu()

        cont = input('Input c to run another function, input anything else to quit\n')
        if cont == 'c' or cont == 'C':
            continue
        else:
            print('Have a good day! :)')
            validity = False

            
#Run the program
main()

