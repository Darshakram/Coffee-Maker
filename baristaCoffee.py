# Main Program
# Project 2: Barista Coffee Assistant
#
# Name: Darcy Eliasi
# Section: 11
# Date: Jan 26
#
from baristaCoffeeFuncs import *


def main():
    coffee = coffee_type()
    size = coffee_size()
    milk = add_milk(coffee)
    location = place()
    cost = total_cost(coffee, size, milk)
    info(coffee, size, milk, location, cost)


if __name__ == '__main__':
    main()
