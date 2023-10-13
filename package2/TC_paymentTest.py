import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentinDollar(self):
        print("payment in dollar")
        self.assertTrue(True)

    def test_paymentinrupees(self):
        print("payment in rupees")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()