import unittest
from list import *

class TestAList(unittest.TestCase):
    def test_list(self):
        self.assertEqual(take_input(6,[1,7,2,2,4,4]),11)

if __name__ == '__main__':
    unittest.main()
