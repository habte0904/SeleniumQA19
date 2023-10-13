import  unittest
from unittest import TestSuite

# import all test case from packages
from package1.TC_loginTestCase import LoginTest
from package1.TC_signUpTestCase import SignUpTest
from package2.TC_paymentTest import PaymentTest
from package2.TC_paymentReturnTest import PaymentReturn

#Get all test from packages
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)

# create test suite
st1 = unittest.TestSuite(tc1)
st2 = unittest.TestSuite(tc2)
ft3 = unittest.TestSuite(tc3)
ft4 = unittest.TestSuite(tc4)

# execute all test suite
unittest.TextTestRunner().run(st2)
unittest.TextTestRunner().run(st1)
unittest.TextTestRunner().run(ft3)
unittest.TextTestRunner().run(ft4)


