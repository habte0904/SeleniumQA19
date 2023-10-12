import unittest


class SkipTestCaseWithCondition(unittest.TestCase):
    x = 5
    y = 0

    def test_add(self):
        self.sum = self.x + self.y
        self.assertEqual(self.sum, 5)

    @unittest.skipIf(x<y, "x must be greater than y")
    def test_sub(self):
        sub = self.x - self.y

    @unittest.skipIf(y == 0, "y must be greater than zero")
    def test_div(self):
        div = self.x / self.y
        self.assertTrue(div)


if __name__ == "__main__":
    unittest.main()
