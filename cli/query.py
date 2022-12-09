"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
import sys
import collections

from data import stock

import time
import datetime
# YOUR CODE STARTS HERE
def filter_data(key,value):
    result = []
    for item in stock:
        if item[key]==value:
            result.append(item)
    return result

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
print('\n' '\n' ,user_name,'Please choose an option: \n- 1.List items by warehouse. \n- 2.Search an item and place an order.\n- 3. search category \n -4.Quit..\n \n:')
menus = (input('Enter 1 ,2 ,3 ,4:     '))
while not menus.isnumeric():
    menus = input('wrong entry: please enter 1,2,3,4')
menu = int(menus)


def menu1():
    total_item_in1 = []
    print('warehouse1')
    for i in stock:
        if i['warehouse'] ==1:
            total_item_in1.append(i)
            print(total_item_in1.index(i)+1,i['state'],i['category'])

    total_item_in2 = []
    print('warehouse2')
    for i in stock:
        if i['warehouse'] ==2:
            total_item_in2.append(i)
            print(total_item_in2.index(i)+1,i['state'],i['category'])
        
    print('**\n****',user_name,'!..' 'Please choose an option: \n- 2.Search an item and place an order.\n- 2.Search Category \n- 4.Quit..\n \n:')
    menu=int(input('Enter 2 ,3 or 4 :'))
    if menu == 2:
        menu2()
    elif menu == 3:
        search_category()
    elif menu ==4:
        print('Thank you for your Visit',user_name+'!')
    if menu not in [2,3,4]:
        print('you are choosing wrong option')




def final_decision():
    opt = input('You do want to add something?Enter y or n:  ')
    if opt == 'y':
        menu2()
    elif opt == 'n':
        print('you are not choosing any other item...Thank you :)')
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
        decision()



def menu2():
    item_name = input('choose an item:   ')
    warehouse1 = []
    warehouse2 = []
    for i in range(len(stock)):
        if stock[i]['state'].upper() in item_name.upper() and stock[i]['category'].upper() in item_name.upper() and stock[i]['warehouse']==1:
            warehouse1.append(stock[i])
            # print(len(warehouse1))
        elif stock[i]['state'].upper() in item_name.upper() and stock[i]['category'].upper() in item_name.upper() and stock[i]['warehouse']==2:
            warehouse2.append(stock[i])

    if item_name in warehouse1 or warehouse2:
        print(item_name, 'found')
        if len(warehouse1) > 0 and len(warehouse2) >0 :
            print('Amount available in both warehouses')
            print('Total Amount available in both warehouses: ' , len(warehouse1)+len(warehouse2))
            if len(warehouse1)< len(warehouse2):
                print('warehouse2 has a larger stock')
                print('Amount available in warehouse2: ',len(warehouse2))
                print('Amount available in warehouse1: ',len(warehouse1))
            elif len(warehouse1)>len(warehouse2):
                print('warehouse1 has a larger stock')
                print('Amount available in warehouse1: ',len(warehouse1))
                print('Amount available in warehouse2: ',len(warehouse2))
            else:
                print('both warehouse has equal stock')
            print('location and days of availability')
            for i in warehouse1:
                delta = datetime.datetime.now()-datetime.datetime.strptime(i['date_of_stock'],'%Y-%m-%d %H:%M:%S')
                print('warehouse1 - is available for ',delta.days,'days')
            for i in warehouse2:
                delta = datetime.datetime.now()-datetime.datetime.strptime(i['date_of_stock'],'%Y-%m-%d %H:%M:%S')
                print('warehouse2 - is available for ',delta.days,'days')


            order=int(input('How many items you want to order?  '))
            if order > len(warehouse1)+len(warehouse2):
                print('There are not this many available. The maximum amount that can be ordered is ',len(warehouse1)+len(warehouse2))
                
                final_decision()
                decision()
            elif order <= len(warehouse1)+len(warehouse2):
                print('You are choosing:  ', item_name)
                decision()
        elif len(warehouse1) > 0 and len(warehouse2) == 0 :
            print('Amount available in warehouse1: ',len(warehouse1))
            print('Location: warehouse1')
        elif len(warehouse1) == 0 and len(warehouse2)> 0 :
            print('Amount available in warehouse2 : ',len(warehouse2))
            print('Location: warehouse2')
    else:
        print('item is not in stock')
        menu2()


  


def search_category():
    
    categories = {1:"Keyboard",2:"Smartphone",3:"Mouse",4:"Laptop",5:"Headphones",6:"Monitor",7:"Router",8:"Tablet"}
    temp = []
    for i in stock:
        counter1 = 0
        for b in categories:
            counter1 += 1
            if i["category"] in categories[counter1]:
                temp.append(counter1)           
    counter = 1
    for i in categories:
        print(f"{i}. {categories[i]} ({temp.count(counter)})")
        counter += 1
    menu_category = int(input("Type the number of the category to browse or press 42 to quit: "))
    if menu_category in range(1,9):
        for i in stock:
            if categories[int(menu_category)] == i["category"]:
                print(i["state"], i["category"],", Warehouse", i["warehouse"])
    elif menu_category == "42":
        pass          

# def menu3():
#     categories = {1:"Keyboard",2:"Smartphone",3:"Mouse",4:"Laptop",5:"Headphones",6:"Monitor",7:"Router",8:"Tablet"}
#     category_list = [item['category'] for item in stock]
#     category_counter = collections.Counter(category_list)
#     print(category_list)
#     print(category_counter)
    


    
        
if menu == 1:
    menu1()

elif menu == 2:
    menu2()
elif menu == 3:
    search_category()
    
elif menu == 4:
    print('')
else:
    print("Invalid input, try 1, 2, or 3")
    
    
       


    




        

    

