import OtpRc4Lib


def main():
    while True:
        user_input = int(input("""
        Select an option:
        1. One-Time Pad Encryption
        2. RC4 Encryption
        3. Exit the program """))
        if user_input == 1:
            # get their plaintext and key
            user_pt_input = input("Please enter your plaintext")
            user_key_input = input("Please enter your key (same length as plaintext)")
            cipherText = OtpRc4Lib.Otp(user_pt_input, user_key_input)
            print("Here is your Ciphertext: \n" + cipherText)

        elif user_input == 2:
            user_pt_input = input("Please enter your plaintext")
            user_key_input = input("Please enter your key")
            cipherText = OtpRc4Lib.Rc4(user_pt_input, user_key_input)
            print("Here is your Ciphertext: \n" + cipherText)

        elif user_input == 3:
            print("goodbye!")
            break


if __name__ == "__main__":
    main()
