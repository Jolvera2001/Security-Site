import string

ALPHABET_LOWERCASE = list(string.ascii_lowercase)
ALPHABET_UPPERCASE = list(string.ascii_uppercase)
SPECIAL_CHARS = list("\\.[]{}()<>*+-=!?^$|,' ")
NUMBERS = list(string.digits)
PLAIN_PATH = "./EDFiles/plaintext.txt"
CIPHER_PATH = "./EDFiles/ciphertext.txt"


def encrypt(key):
    n = int(key)
    file_contents = ""
    cipherString = ""
    with open(PLAIN_PATH, 'r') as file:
        file_contents = file.read()

    # File is closed, so now we use the shift key
    for char in file_contents:
        if char.isupper():
            char_index = ALPHABET_UPPERCASE.index(char)
            char = ALPHABET_UPPERCASE[(char_index + n) % 26]
            cipherString += char
        elif char.islower():
            char_index = ALPHABET_LOWERCASE.index(char)
            char = ALPHABET_LOWERCASE[(char_index + n) % 26]
            cipherString += char
        elif char.isdigit():
            char_index = NUMBERS.index(char)
            char = NUMBERS[(char_index + n) % 9]
            cipherString += char
        elif char in SPECIAL_CHARS:
            char_index = SPECIAL_CHARS.index(char)
            char = SPECIAL_CHARS[(char_index + n) % len(SPECIAL_CHARS)]
            cipherString += char
        else:
            cipherString += char

    # Put it file contents into Cyphertext
    with open(CIPHER_PATH, 'w') as file:
        file.write(cipherString)


def decrypt(key):
    n = int(key)
    file_contents = ""
    plainString = ""
    with open(CIPHER_PATH, 'r') as file:
        file_contents = file.read()

    # File closed, now work backwards
    for char in file_contents:
        if char.isupper():
            char_index = ALPHABET_UPPERCASE.index(char)
            char = ALPHABET_UPPERCASE[(char_index - n) % 26]
            plainString += char
        elif char.islower():
            char_index = ALPHABET_LOWERCASE.index(char)
            char = ALPHABET_LOWERCASE[(char_index - n) % 26]
            plainString += char
        elif char.isdigit():
            char_index = NUMBERS.index(char)
            char = NUMBERS[(char_index - n) % 9]
            plainString += char
        elif char in SPECIAL_CHARS:
            char_index = SPECIAL_CHARS.index(char)
            char = SPECIAL_CHARS[(char_index - n) % len(SPECIAL_CHARS)]
            plainString += char
        else:
            plainString += char

    # Put it file contents into plaintext
    with open(PLAIN_PATH, 'w') as file:
        file.write(plainString)


def brute_force():
    print("Placeholder")
