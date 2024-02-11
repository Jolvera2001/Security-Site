def otp(pt, key):
    print(pt, key)

def rc4(pt, key):
    '''
    We need to use otp at the end when the
    shortkey is lengthended to the size of the pt
    1. Extend key
    2. otp with extended key
    '''
    print(pt, key)