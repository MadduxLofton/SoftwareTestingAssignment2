"""
this block is from
https://docs.python.org/3/library/unittest.html


import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
"""

import unittest
import SW_Testing_assignment_2 as main
class TestBMIProgram(unittest.TestCase):
    def test_BMI_classification(self):
        self.assertEqual(main.classify(18.4), "Underweight")
        self.assertEqual(main.classify(18.5), "Normal weight")
        self.assertEqual(main.classify(24.9), "Normal weight")
        self.assertEqual(main.classify(25), "Overweight")
        self.assertEqual(main.classify(29.9), "Overweight")
        self.assertEqual(main.classify(30), "Obese")
        

if __name__ == '__main__':
    unittest.main()

