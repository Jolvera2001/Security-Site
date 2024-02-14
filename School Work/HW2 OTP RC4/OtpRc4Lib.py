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

    # putting 0-255 in s
    # putting repeated Key chars 256 times
    # chars are converted to ascii to properly add onto ints
    for i in range(256):
        s.append(i)
        k.append(ord(key[i % len(key)]))

    j = 0
    for i in range(256):
        j = (j + s[i] + k[i]) % 256
        s[i] = s[j]

    i = j = 0

    # KBG
    keystream_word = ""

    while len(keystream_word) != len(pt):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        t = (s[i] + s[j]) % 256

        # change num into character with chr and ord
        keystream_word += chr(s[t])

    # then we send through OTP
    encrypted = otp(pt, keystream_word)

    return encrypted


