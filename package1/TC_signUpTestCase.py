import unittest


class SignUpTest(unittest.TestCase):

    def test_SignByEmail(self):
        print("SignUp the page with Email account")
        self.assertTrue(True)

    def test_SignUpByFacebook(self):
        print("SignUp the page with Facebook account")
        self.assertTrue(True)

    def test_SignUpByGithub(self):
        print("SignUp the page with github account")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()