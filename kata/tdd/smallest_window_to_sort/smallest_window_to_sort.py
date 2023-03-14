'''

Test cases:

  - empty array
    [] -> (None, None)
  - array with one element
    [10] -> (None, None)
  - already sorted array
    [1, 2, 3, 4, 5] -> (None, None)
  - reverse sorted array
    [5, 4, 3, 2, 1] -> (0, 4)
  - array with same element
    [7, 7, 7, 7, 7, 7] -> (None, None)
  - array with two elements in the middle out of order
    [1, 2, 4, 3, 5] -> (2, 3)
  - array with elements out of order at the beginning
    [2, 1, 3, 4, 5] -> (0, 1)
  - array with repeated elements
    [1, 5, 5, 4, 3, 3, 6] -> (1, 5)
'''
import unittest
from parameterized import parameterized, parameterized_class

def smallest_window_to_sort_with_sorted(nums):
    left, right = None, None
    s = sorted(nums)

    for i in range(len(nums)):
        if nums[i] != s[i] and left is None:
            left = i
        elif nums[i] != s[i]:
            right = i
    return (left, right)

def smallest_window_to_sort(nums):
    left, right = None, None
    max_seen, min_seen = -float("inf"), float("inf")
    n = len(nums)

    for i in range(n):
        if max_seen < nums[i]:
            max_seen = nums[i]
        if nums[i] < max_seen:
            right = i

    for i in range(n-1, -1, -1):
        if min_seen > nums[i]:
            min_seen = nums[i]
        if nums[i] > min_seen:
            left = i

    return left, right

@parameterized_class(("function_to_test",), 
                     [
                        (staticmethod(smallest_window_to_sort), ),
                        (staticmethod(smallest_window_to_sort_with_sorted), ),
                     ])
class TestSmallestWindowToSortFunction(unittest.TestCase):
    @parameterized.expand([
        ("empty_array", [], (None, None)),
        ("array_with_one_element", [10], (None, None)),
        ("already_sorted_array", [1, 2, 3, 4, 5], (None, None)),
        ("reverse_sorted_array", [5, 4, 3, 2, 1], (0, 4)),
        ("array_with_repeated_element", [7, 7, 7, 7, 7, 7], (None, None)),
        ("arrawy_with_two_elements_in_middle_out_of_order", [1, 2, 4, 3, 5], (2, 3)),
        ("arrawy_with_elements_out_of_order_at_beginning", [2, 1, 3, 4, 5], (0, 1)),
        ("arrawy_with_repeated_elements_out_of_order", [1, 5, 5, 4, 3, 3, 6], (1, 5)),
    ])
    def test_it(self, name, input, expected):
        func = self.function_to_test
        result = func(input)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
