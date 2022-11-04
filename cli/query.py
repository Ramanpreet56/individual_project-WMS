"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from ast import Break
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
print('')
print('\n' '\n' ,user_name,'Please choose an option: \n- 1.List items by warehouse. \n- 2.Search an item and place an order.\n- 3.Quit..\n \n:')
menu=int(input('Enter 1 ,2 or 3 :'))



# If they pick 1
def item_count(item , warehouse):
    count = 0
    for x in warehouse:
        if item == x:
            count = count+1
    return count

def print_list(list):
    for x in list:
        print(x,'\n')

def final_decision():
    opt = input('You do want to add something?Enter y or n:  ')
    if opt == 'y':
        item_search()
    elif opt == 'n':
        print('you are not choosing any other item...')
    else:
        print('please choose y or n')
        final_decision()




def decision():
                buyout_decision = input('proceed to buy? Enter y for buying or n for exit:  ')
                if buyout_decision == 'y':
                    
                    print('Thank you for choosing us..your order is placed..', user_name ,'!')
                    
                    
                    final_decision()           
                elif buyout_decision =='n':
                    print('Thank you for your visit',user_name)
                else:
                    print('Please enter y or n')

def item_search():
    item= str.capitalize(input('Choose an item: '))
    
    if item in warehouse1 or item in warehouse2:
        print(item,'was found')
        count_warehouse1 = item_count(item,warehouse1)
        count_warehouse2 = item_count(item,warehouse2)

        if count_warehouse1 > 0 and count_warehouse2 >0 :
            print('Amount available: ',count_warehouse1+count_warehouse2)
            print('Location: warehouse1 and warehouse2')
        elif count_warehouse1 == 0 and count_warehouse2 >0 :
            print('Amount available: ',count_warehouse1+count_warehouse2)
            print('Location: warehouse2')
        elif count_warehouse1 > 0 and count_warehouse2 == 0 :
            print('Amount available: ',count_warehouse1+count_warehouse2)
            print('Location: warehouse1')
        order=int(input('How many items you want to order?  '))
        if order > count_warehouse1+count_warehouse2:
            print('There are not this many available. The maximum amount that can be ordered is ',count_warehouse1+count_warehouse2)
            decision()
            final_decision()
        elif order <= count_warehouse1+count_warehouse2:
            print('You are choosing:  ', item)
            decision()


          
# Thank the user for the visit
            
    else: 
        print(item,'was not found,try again...')
        item_search()
        


if menu == 1:
    print('The items in warehouse1 are:     ','\n')
    print_list(set(warehouse1))
    print('')
    print('The items in warehouse2 are:     ','\n')
    print_list(set(warehouse2))
    print('')
    print('**********************')
    print('**\n****',user_name,'!..' 'Please choose an option: \n- 2.Search an item and place an order.\n- 3.Quit..\n \n:')
    menu=int(input('Enter 2 or 3 :'))
    if menu == 2 and 3:
        item_search()
    if menu not in [2,3]:
        print('you are choosing wrong option')
    
    
# Else, if they pick 2

elif menu == 2:
    print('choose an item and place an order', user_name)
    item_search()

# Else, if they pick 3
elif menu == 3: 
    print('Thank you for your visit,', user_name,'!')

else:
    print('Invalid input')


        

    

