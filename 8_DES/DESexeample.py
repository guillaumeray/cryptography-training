from pyDes import *

"""
We import an implementation of DES in python to use it
We'll not analyse DES implementation because it's complicated
We can try to play with it to understand

* ECB mode
We have three block of 8 size
The two first block are identical
It make sense bacause the message is identical from 0 to 8 and from 8 to 16
IV vector is ignored

* CBC mode
We have three block of 8 size
All block are different event if we have same pattern in message
We use IV vector in the process of encryption
"""

message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)

cipher = k.encrypt(message)
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher[0:8])
print("Encrypted:", cipher[8:16])
print("Encrypted:", cipher[16:])
message = k.decrypt(cipher)
print("Decrypted:", message)

"""
What happen if we try to change each bit of cipher like stream cipher ? 
Actually if we change one bit on the first 8bit block it will break the first block.
It's not possible to change one letter, we have to change all the block.
"""
message = "SEND ALICE 10$ and give it to bob"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
cipher = k.encrypt(message)

def modify(cipher):
    mod = [0]*len(cipher)
    mod[8] = 1
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

cipher = modify(cipher)
print(cipher)
message = k.decrypt(cipher)
print("Decrypted:", message)

