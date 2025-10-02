import unittest
from function import newadd

class TestFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(-3, -7), -4)

if __name__ == "__main__":
    unittest.main()
