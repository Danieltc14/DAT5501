import unittest
from function import newadd

class TestFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(newadd(-1, 1), 0)
        self.assertEqual(newadd(1, 0), 1)
        
if __name__ == "__main__":
    unittest.main()
