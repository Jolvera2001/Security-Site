import OtpRc4Lib


def main():
    while True:
        user_input = int(input("""
        Select an option:
        1. One-Time Pad Encryption
        2. RC4 Encryption
        3. Exit the program """))
        if user_input == 1:
            print("OTP Ran")
        elif user_input == 2:
            print("RC4 Ran")
        elif user_input == 3:
            print("goodbye!")
            break


if __name__ == "__main__":
    main()
