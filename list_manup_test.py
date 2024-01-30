import unittest
from list_manup import manipulate_list

class TestListManipulator(unittest.TestCase):
    def test_valid_input(self):
        # Test with a valid input list
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = manipulate_list(input_list)
        expected_result = [1, 4, 5, 7, 8, 11, 13, 14, 17, 19]
        self.assertEqual(result, expected_result)

    def test_invalid_length(self):
        # Test with an invalid input list length
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(ValueError):
            manipulate_list(input_list)

if __name__ == '__main__':
    unittest.main()

