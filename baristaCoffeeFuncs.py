# Functions (have at least 4 functions)
# Project 2: Barista Coffee Assistant
#
# Name: Darcy Eliasi
# Section: 11
# Date: Jan 26
#

# Checks to see what the coffee type the customer wants
# none --> str
def coffee_type():
    coffee = input("What coffee type would you like?")
    problems = 0
    while (coffee != "Americano") and (coffee != "Flat White") and (coffee != "Espresso") and (coffee != "Latte"):
        problems += 1
        if problems < 3:
            coffee = input("Can you please try again?")
        else:
            print("Sorry, we cannot help you here.")
            exit()
    return coffee


# Checks to see what the coffee size the customer wants
# none --> str
def coffee_size():
    size = input("What size do you want [Large, Medium, Small]?")
    problems = 0
    while (size != "Large") and (size != "Medium") and (size != "Small"):
        problems += 1
        if problems < 3:
            size = input("Can you please try again?")
        else:
            print("Sorry, we cannot help you here.")
            exit()
    return size


# Checks to see if the customer wants milk with their coffee if they got an Americano or Espresso
# none --> str
def add_milk(coffee):
    if (coffee == "Americano") or (coffee == "Espresso"):
        milk = input("Would you like milk on the side [y, n]?")
        problems = 0
        while (milk != "y") and (milk != "n"):
            problems += 1
            if problems < 3:
                milk = input("Can you please try again?")
            else:
                print("Sorry, we cannot help you here.")
                exit()
        if milk == "y":
            return "Milk on the side"
        else:
            return "No extras"
    return "No extras"


# Checks to see if the customer wants to dine in or take out
# none --> str
def place():
    location = input("Is your coffee takeout [y, n]?")
    problems = 0
    while (location != "y") and (location != "n"):
        problems += 1
        if problems < 3:
            location = input("Can you please try again?")
        else:
            print("Sorry, we cannot help you here.")
            exit()
    if location == "y":
        return "Takeout"
    else:
        return "In cafe"


# calculates the final price of the coffee from what the costumer ordered
# strstrstr --> float
def total_cost(coffee, size, milk):
    cost = 0
    if coffee == "Flat White":
        if size == "Small":
            cost = 2.95
        elif size == "Medium":
            cost = 3.00
        else:
            cost = 3.75
    if coffee == "Latte":
        if size == "Small":
            cost = 2.85
        elif size == "Medium":
            cost = 3.75
        else:
            cost = 4.15
    if (coffee == "Americano") or (coffee == "Espresso"):
        if size == "Small":
            cost = 2.75
        elif size == "Medium":
            cost = 2.95
        else:
            cost = 3.25
        if milk == "Milk on the side":
            cost += 0.25
    return cost


# Repeats the order and gives a final price
# strstrstrstrfloat --> strstrstrstrfloat
def info(coffee, size, milk, location, cost):
    print(coffee)
    print(milk)
    print(location)
    print("Please pay $%3.2f to the cashier." % cost)
