'''
Create a file called test_cities.py that tests the function you just wrote 
(remember that you need to import unittest and the function you want to test). 
Write a method called test_city_country() to verify that calling your function with values such as Santiago and Chile 
results in the correct string. Run test_cities.py, and make sure test_city_country() passes.
 When it passes, take a screenshot of the result and paste in into your Word document.
 '''

import unittest
from city_functions import get_formatted_name

#Format below adapted from:
#Python Crash Course: A Hands-On, Project-Based Introduction to Programming, 2nd Edition
#by Eric Matthes
#Chapter 11 test_name_function.py

class NamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        formatted_name = get_formatted_name('santiago', 'ChIlE')
        self.assertEqual(formatted_name, 'Santiago, Chile')

if __name__ == '__main__':
       unittest.main()