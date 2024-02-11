import ccLib

# Using Python 3.12
def main():
    while True:
        user_input = int(input("""
        Select an option:
        1. Encrypt Message
        2. Decrypt Message
        3. Break
        4. Exit the program 
        """))
        if user_input == 1:
            # Ask for Key value n
            user_n_input = ""

            while not user_n_input.isnumeric():
                user_n_input = input("Enter your key N: ")

            ccLib.encrypt(user_n_input)
            print("Encrypted")

        elif user_input == 2:
            # Ask for Key value n
            user_n_input = ""

            while not user_n_input.isnumeric():
                user_n_input = input("Enter your key N: ")

            ccLib.decrypt(user_n_input)
            print("Decrypted")

        elif user_input == 3:
            # Break into encryption
            ccLib.brute_force()

        elif user_input == 4:
            # Exit
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
