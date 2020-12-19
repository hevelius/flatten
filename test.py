import unittest

from utils import *

class TestFlatten(unittest.TestCase):
    def test_if_list_has_sublist(self):
        """
        Test if list has sublist
        """
        data = random_list()
        result = flatten(data)
        for i in result:
            self.assertNotIsInstance(i, list)
        
    def test_if_result_is_list(self):
        """
        Test if result is a list
        """
        data = random_list()
        result = flatten(data)
        self.assertIsInstance(result, list)
    
    def test_if_list_flattened(self):
        """
        Test if result is flattened
        """
        data = [[1,2,[3]],4]
        expected = [1,2,3,4]
        result = flatten(data)
        self.assertListEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
