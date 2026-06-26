import unittest
from main import say_hello

class TestHelloPatil(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello Kaushik")

if __name__ == "__main__":
    unittest.main()
