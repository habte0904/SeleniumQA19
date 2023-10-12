import unittest


class skipTestCase(unittest.TestCase):
    # skip test case without reason
    @unittest.skip
    def test_edge(self):
        print("from edge browser")

    # skip test case with a reason
    @unittest.skip("We want to skip chrome browser test")
    def test_chrome(self):
        print("from chrome browser")

    def test_Firefox(self):
        print("from firefox browser")

    def test_safari(self):
        print("from safari browser")



if __name__ == "__main__":
    unittest.main()
