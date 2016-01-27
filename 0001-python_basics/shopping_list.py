def greeting():
    print(" ")
    print("Enter an item for your shopping list and press <RETURN> or <ENTER>.")
    print(" ")
    print("When you're finished adding items to your shopping list,")
    print("type DONE and press <RETURN> or <ENTER>.")
    print(" ")

def get_input():
    return input("Item: ")

def print_it(shopping_list):
    print(" ")
    print("Your Shopping List:")
    for item in shopping_list:
        print(" > " + item)
    print(" ")

def show_help():
    print(" ")
    print("Type DONE when you are finished entering items in your shopping list.")
    print("We'll show your final shopping list and then exit the program.")
    print(" ")
    print("Type SHOW to see your shopping list.  You can continue entering items")
    print("after viewing it.")
    print(" ")
    print("Type HELP to see this list of valid commands.")
    print(" ")


# app starts here
greeting()

shopping_list = []

finished = False
while finished != True:
    item = get_input()
    if item == "DONE":
        finished = True
    elif item == "SHOW":
        print_it(shopping_list)
    elif item == "HELP":
        show_help()
    else:
        shopping_list.append(item)

# print the shopping list
print_it(shopping_list)
