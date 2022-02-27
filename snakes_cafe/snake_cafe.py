# print("**************************************")
# print("**    Welcome to the Snakes Cafe!   **")
# print("**    Please see our menu below.    **")
# print("**")
# print('** To quit at any time, type "quit" **')
# print("**************************************")
# Not a good Practice above ...)

# Assigning
cafe_menue = ["wings", "cookies", "spring", "rolls", "salmon", "meat tornado",
              "a literal garden", "ice cream ", "cake", "pie", "coffe", "tea", "unicorn tears"]
order_list = {}
quantity = 1
# printing the interface
print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')

while True:
    user_input = input(">").lower()
    if user_input == "quit":
        break
    elif user_input in cafe_menue:
        if user_input in order_list:
            quantity += 1
        else:
            quantity = 1
        order_list.update({user_input: quantity})
        # print(order_list)
        # Should i make obj/dictionary? better? key:value? food:quantity?
        # .count ? of how many the user input + check if in ??? /OR/
        # quantity = len(order_list)
        # print("1", order_list)
        # print("2", user_input)
        print(
            f'\n** {quantity} order of {user_input} have been added to your meal**\n')
    else:
        print(
            f"unfortunately,this item ({user_input}) is not availabe on the menu, Kindly Choose another! \n")
