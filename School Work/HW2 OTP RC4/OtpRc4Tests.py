import unittest
import OtpRc4Lib as OR


class OtpUnitTests(unittest.TestCase):

    def test_opt_basic(self):
        string1 = "Hello World!"
        key1 = "somet hinga!"
        string2 = "I hope this ends up super well! wishing for the best"
        key2 = "i h035 ajwewwdwg gr super nniei w1dhiapgbii19n89i3st"
        string3 = "...."
        key3 = "4444"

        cipher1 = OR.otp(string1, key1)
        cipher2 = OR.otp(string2, key2)
        cipher3 = OR.otp(string3, key3)

        self.assertTrue(OR.otp(cipher1, key1) == string1)
        self.assertTrue(OR.otp(cipher2, key2) == string2)
        self.assertTrue(OR.otp(cipher3, key3) == string3)

    def test_Rc4_basic(self):
        string1 = "Hello World!"
        key1 = "awz"
        string2 = "I hope this ends up super well! wishing for the best"
        key2 = "wack"
        string3 = "...."
        key3 = "1"

        cipher1 = OR.rc4(string1, key1)
        cipher2 = OR.rc4(string2, key2)
        cipher3 = OR.rc4(string3, key3)

        self.assertTrue(OR.rc4(cipher1, key1) == string1)
        self.assertTrue(OR.rc4(cipher2, key2) == string2)
        self.assertTrue(OR.rc4(cipher3, key3) == string3)


if __name__ == "__main__":
    unittest.main()