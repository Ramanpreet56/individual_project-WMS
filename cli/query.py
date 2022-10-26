"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2
import time

# YOUR CODE STARTS HERE

print('')
print('WMS- Warehouse management system')
print('-')

# Get the user name
user_name = input('Please provide your name:  ')
print('')
# Greet the user

print('welcome',user_name)


# Show the menu and ask to pick a choice

print(user_name,'Please choose an option: \n- 1.List items by warehouse \n- 2.Search an item and place an order \n- 3.Quit\n \n:')
menu=int(input('Enter 1 ,2 or 3 :'))
if menu not in [1,2,3]:
    print('Invalid input')

# If they pick 1
def item_search():
    item=input('Choose an item: ')
    
    if item in warehouse1 or item in warehouse2:
        print(item,'was found')
# Thank the user for the visit
        buyout_decision = input('proceed to buy? Enter y for buying or n for exit:  ')
        if buyout_decision == 'y':
            print('Thank you and visit us again',user_name)
        elif buyout_decision =='n':
            print('Thank you for your visit',user_name)
        else:
            print('Please enter y or n')
    else: 
        print(item,'was not found')



if menu == 1:
    print('The items in warehouse1 are:     ', warehouse1)
    print('')
    print('The items in warehouse2 are:     ',warehouse2)
    item_search()
# Else, if they pick 2

elif menu == 2:
   item_search()

# Else, if they pick 3
elif menu == 3: 
    print('')
        

    

