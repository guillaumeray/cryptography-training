from pyDes import *
import random

"""
Let's see an brute force attack on DES
We reduced the key space to brute force to 2**8 (8 bits) to
do it faster. Actually with some power we can brute force key up to 32 bits.
"""

message = "01234567"
key_11 = random.randrange(0, 256)
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])
iv = bytes([0]*8)

k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)

# Alice sending encrypted message
cipher = k1.encrypt(message)
print("Key 1: ", key_11)
print("Encrypted: ", cipher)

# This is Bob
message = k1.decrypt(cipher)
print("Decrypted: ", message)

# Eve's attack on DES
"""
We loop for 2**8 = 256 possibility to get the good key
For most key value k.decrypt will return empty result, in python lookup[""] is skipped
That's why for 256 try the len of lookup can be 10.
The good result is easily find in the lookup list
"""
print("Brute force attack for key :")
lookup = {}
for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    lookup[k.decrypt(cipher)] = i

for l in lookup:
    print("key:", lookup[l], l)

"""
Then if the keyspace is low we can easily bruteForce DES 
"""

"""
We can do the same attack with double DES
Thanks to meet in the midle algorithm
"""
print()
print("DOUBLE DES example : ")

message = "01234567"
key_11 = random.randrange(0, 256)
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])
key_21 = random.randrange(0, 256)
key_2 = bytes([key_21, 0, 0, 0, 0, 0, 0, 0])

iv = bytes([0]*8)
k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)

"""
We encrypt the message two time with two different keys
k1.encrypt(k2.encrypt(message))
We encrypted an encrypted message

To decrypt we decrypt ciphered with k1 we get a ciphered message
Then we decrypt this ciphered with k2 to get the plain text
"""

# Alice sending encrypted message
cipher = k1.encrypt(k2.encrypt(message))
print("Key 1: ", key_11)
print("Key 2: ", key_21)
print("Encrypted: ", cipher)

# This is Bob
message = k2.decrypt(k1.decrypt(cipher))
print("Decrypted: ", message)

# Eve's attack on DES
"""
We have to know the plain text message to do this attack
This attack show that double DES do not double the bit security 
We can still brute force with 2**9

We loop in 256 possibility to get the encrypted message with related key
We loop again in 256 possibility and check in k.decrypt match with k.encrypt
Thats mean than we found the intermediate encryption of the cipher. 
If match we found the two key 
"""
lookup = {}
for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    lookup[k.encrypt(message)] = i

for i in range(256):
    key = bytes([i, 0, 0, 0, 0, 0, 0, 0])
    k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
    if k.decrypt(cipher) in lookup:
        print("Key 11:", i)
        print("Key 21:", lookup[k.decrypt(cipher)])
        key_1 = bytes([i, 0, 0, 0, 0, 0, 0, 0])
        key_2 = bytes([lookup[k.decrypt(cipher)], 0, 0, 0, 0, 0, 0, 0])
        k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
        k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)
        print("Eve break double DES", k2.decrypt(k1.decrypt(cipher)))
        break

"""
Double DES can be weak in term of key space that's why we use triple DES instead
"""