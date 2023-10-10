import unittest
from selenium import webdriver


class AssertionMethod(unittest.TestCase):
    def test_simpleAssertion(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.titles = self.driver.title
        print("Title of the page= " + self.titles)
        self.assertEqual("Google", self.titles, "Title is not correct")
        self.assertNotEqual("google", self.titles, "Title is correct")
        self.a = 6
        self.b = 4
        # self.assertEqual(self.a, self.b, "a is different from b values")
        self.assertNotEqual(self.a, self.b, "a is  equal to b")

        self.assertTrue(self.titles == "Google", "Assert is fail if both value are not equal")
        self.assertFalse(self.titles == "Ghoogle", "it's fail, when both values are equal")


if __name__ == "__main__":
    unittest.main()
