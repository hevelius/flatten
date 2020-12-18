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
            if isinstance(i,list):
                self.fail("result contains sublist")
    
    def test_if_result_is_list(self):
        """
        Test if result is a list
        """
        data = random_list()
        result = flatten(data)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
