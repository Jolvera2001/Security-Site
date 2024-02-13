def otp(pt, key):
    if len(key) != len(pt):
        return "Pt and Key are not the same size!"

    # doing the xor for each character
    cipher_text = ""
    for i in range(len(pt)):
        pt_char = ord(pt[i])
        key_char = ord(key[i])
        cipher_text += chr(pt_char ^ key_char)

    return cipher_text


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
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    t = (s[i] + s[j]) % 256

    # change num into character with chr and ord
    keystream_Byte = s[t]


