import unittest


# create class
class PythonUnittest(unittest.TestCase):
    # create method
    def test1(self):
        print("python unittest first code!")

    def test2(self):
        print("from test2")


# run unittest code from unittest main method
if __name__ == "__main__":
    unittest.main()
