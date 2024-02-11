import unittest
import OtpRc4Lib as OR


class OtpUnitTests(unittest.TestCase):

    def test_opt_basic(self):
        string1 = "Hello World!"
        key1 = "yellow borld"
        string2 = "h3llo w0rld!"
        key2 = "12345 67890!"
        string3 = "th1s ' is weirdn nn"
        key3 = "1234 ; we dfenfn nn"

        throwaway1, check1 = OR.otp(string1, key1)
        throwaway2, check2 = OR.otp(string2, key2)
        throwaway3, check3 = OR.otp(string3, key3)

        self.assertEqual(check1, string1)
        self.assertEqual(check2, string2)
        self.assertEqual(check3, string3)

if __name__ == "__main__":
    unittest.main()