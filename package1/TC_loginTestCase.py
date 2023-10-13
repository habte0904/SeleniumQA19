import unittest


class LoginTest(unittest.TestCase):

    def test_loginByEmail(self):
        print("login the page with Email account")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("login the page with Facebook account")
        self.assertTrue(True)

    def test_loginByGithub(self):
        print("login the page with github account")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()