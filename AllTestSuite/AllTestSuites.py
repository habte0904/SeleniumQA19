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


