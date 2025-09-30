import unittest


class ExampleTest(unittest.TestCase):
    def test_sample(self):
        result = 2 == 3
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
