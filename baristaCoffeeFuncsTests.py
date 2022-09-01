# Function Tests Program
# Project 2: Barista Coffee Assistant
#
# Name: Darcy Eliasi
# Section: 11
# Date: Jan 26
#
from baristaCoffeeFuncs import *
import unittest
class MyTestCase(unittest.TestCase):
    def test_total_cost(self):
        self.assertEqual(total_cost("Americano", "Small", "Milk on the side"), 3.0)
        self.assertEqual(total_cost("Americano", "Medium", "Milk on the side"), 3.20)
        self.assertEqual(total_cost("Americano", "Large", "Milk on the side"), 3.50)
        self.assertEqual(total_cost("Americano", "Small", "No extras"), 2.75)
        self.assertEqual(total_cost("Americano", "Medium", "No extras"), 2.95)
        self.assertEqual(total_cost("Americano", "Large", "No extras"), 3.25)

        self.assertEqual(total_cost("Espresso", "Small", "Milk on the side"), 3.0)
        self.assertEqual(total_cost("Espresso", "Medium", "Milk on the side"), 3.20)
        self.assertEqual(total_cost("Espresso", "Large", "Milk on the side"), 3.50)
        self.assertEqual(total_cost("Espresso", "Small", "No extras"), 2.75)
        self.assertEqual(total_cost("Espresso", "Medium", "No extras"), 2.95)
        self.assertEqual(total_cost("Espresso", "Large", "No extras"), 3.25)

        self.assertEqual(total_cost("Latte", "Small", "No extras"), 2.85)
        self.assertEqual(total_cost("Latte", "Medium", "No extras"), 3.75)
        self.assertEqual(total_cost("Latte", "Large", "No extras"), 4.15)

        self.assertEqual(total_cost("Flat White", "Small", "No extras"), 2.95)
        self.assertEqual(total_cost("Flat White", "Medium", "No extras"), 3.00)
        self.assertEqual(total_cost("Flat White", "Large", "No extras"), 3.75)




if __name__ == '__main__':
    unittest.main()
