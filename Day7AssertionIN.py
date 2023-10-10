import unittest


class AssertionIN(unittest.TestCase):
    def test_simpleTest(self):
        self.list = {3, 5, 8, 9, 10}
        self.assertIn(5, self.list, "value is not in the list")
        self.assertIn(7, range(6), "value is not exist in the range")
    def test_AssertNotIN(self):
        self.language = {"python", "java", "Selenium", "Testing"}
        self.assertNotIn("Python", self.language, "value exist in the list")



if __name__ == "__main__":
    unittest.main()
