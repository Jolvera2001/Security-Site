import base64


def otp(pt, key):
    # TODO: Implement to where the function only returns one, but do it twice
    # on the main
    if len(key) != len(pt):
        return "Pt and Key are not the same size!"

    # doing the xor for each character
    cipher_text = ""
    for i in range(len(pt)):
        pt_char = ord(pt[i])
        key_char = ord(key[i])
        cipher_text += chr(pt_char ^ key_char)

    checked_text = ""
    for i in range(len(cipher_text)):
        cipher_char = ord(cipher_text[i])
        key_char = ord(key[i])
        checked_text += chr(cipher_char ^ key_char)

    if checked_text == pt:
        return cipher_text, checked_text
    else:
        # debugging purposes
        print("Something went wrong")
        return "None", "None"


def rc4(pt, key):
    # Initialization
    s = []
    k = []

    for i in range(256):
        s[i] = i
        k[i] = key[i % len(key)]

    j = 0
    for i in range(256):
        j = (j + s[i] + k[i]) % 256
        s[i] = s[j]

    i = j = 0
    # KBG

