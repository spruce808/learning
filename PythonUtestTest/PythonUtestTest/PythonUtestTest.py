import unittest

class MyTestClass(unittest.TestCase):
    """Simple test class
    """

    def test_me(self):
        self.assertTrue(True)

    def test_me_too(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

