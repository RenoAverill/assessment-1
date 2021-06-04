# import unittest library
import unittest
import optimal_change


class TestStringMethods(unittest.TestCase):
    # tests the correct result
    def test_propper_result(self):
        change = optimal_change(62.13, 100)
        result = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        self.assertEqual(change, result)
    # checks the correct result
    def test_correct_output(self):
        change = optimal_change(31.51, 50)
        result = "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
        self.assertEqual(change, result)
    # checks if the type of result is string
    def test_is_string(self):
        end_statement = type(optimal_change(10,10)) == str
        self.assertTrue(end_statement)
    # checks function within my method to see if the correct change is correct
    def test_correct_change_amount(self):
        change = optimal_change(10, 50).change_due(10, 50)
        self.assertEqual(change, 40)
    # tests the last puncuation of pennies Plural or Singular
    def test_puncuation(self):
        plural_pennies = optimal_change(10, 9.98)
        self.assertEqual(plural_pennies, 'pennies')






if __name__ == '__main__':
    unittest.main()