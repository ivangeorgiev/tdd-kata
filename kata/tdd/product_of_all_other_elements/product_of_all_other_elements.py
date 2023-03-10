"""
Given an array of integers, return a new array such that each element at index i of 
the new array is the product of all the numbers in the original array except the one 
at i.

For example, if our input was [ 1, 2, 3, 4, 5], the expected output would be [ 120, 
60, 40, 30, 24]. Ifourinputwas [3, 2, 1],theexpectedoutputwouldbe [2, 
3, 6]. 

Follow-up: What if you can't use division?
"""

from functools import reduce
import unittest

def product_of_previous_elements(nums):
    product_of_previous = 1
    for num in nums:
        yield product_of_previous
        product_of_previous = product_of_previous*num

def product_of_all_other_elements(nums):
    assert len(nums) > 1, f"'nums' should have at least 2 elements. {len(nums)} given."
    products = list(product_of_previous_elements(nums))
    for index_from_end, product_after in enumerate(product_of_previous_elements(reversed(nums))):
        products[-index_from_end - 1] *= product_after
    return products

class TestProductOfPreviousElementsFunction(unittest.TestCase):
    def test_should_return_list_with_value_one_input_list_with_one_element(self):
        # Setup
        nums = [8]
        # Act
        result = list(product_of_previous_elements(nums))
        # Assert
        self.assertEqual(result, [1])

    def test_product_of_previous_should_return_list_with_product_of_previous_elements(self):
        # Setup
        nums = [5, 7, 8]
        # Act
        result = list(product_of_previous_elements(nums))
        # Assert
        self.assertEqual(result, [1, 5, 35])


class TestProductOfAllOtherElementsFunction(unittest.TestCase):
    def test_should_raise_AssertionError_input_empty_list(self):
        nums = []
        with self.assertRaises(AssertionError) as assert_context:
            product_of_all_other_elements(nums)
        self.assertEqual(str(assert_context.exception), "'nums' should have at least 2 elements. 0 given.")

    def test_should_raise_AssertionError_input_single_element(self):
        nums = [77]
        with self.assertRaises(AssertionError) as assert_context:
            product_of_all_other_elements(nums)
        self.assertEqual(str(assert_context.exception), "'nums' should have at least 2 elements. 1 given.")


    def test_should_return_list_of_products_of_all_other_elements(self):
        nums = [1, 3, 5, 8]
        result = product_of_all_other_elements(nums)
        self.assertEqual(result, [120, 40, 24, 15])

if __name__ == '__main__':
    unittest.main()

