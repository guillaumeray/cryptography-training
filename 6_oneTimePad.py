import random

"""
XOR function has good cryptographic property
It's an easy binary operation than the computer can do billion of time 
And it can be used as a symetric key (same key to encrypt and decrypt)
"""

"""
INTRODUCTION
Understanding of string encodage to binary
Let's cypher one letter in ASCII with XOR
"""
letter = "z"
"""
The letter z can be represented in hexadecimal with ascii encodage
"""
res = bytes(letter, 'ascii')
print("letter z is hex : ", res.hex())
"""
The letter z hex representation is 7a wich is 122 int (see ascii table) wich is 01111010 bin
"""
print("letter z is bin : ",bin(int(res.hex(), 16)))
"""
Let's cipher the letter with a key equal to 65 int > 41 hex > 1000001 bin
 01111010 (122)
 01000001 (65)
=00111011 (59)
"""
print("122 XOR 65 is ", 122 ^ 65)

"""
122^65 = 59, if we look at ascii code table it correspond to the letter ";"
"""

"""
The key is 65 then to get back the original letter we can do 59 ^ 65 = 122
(!) We can also get the key if we have the original letter and the ciphered (!) 122 ^ 59 = 65
(!!) But if we do not have the key there is no clue to guess it because every key ^ ciphered can return good result (!!)
(!!) For example ciphered 59 ^ guess key 63 = 4 wich is the number 4 in ascii code table (!!)
To remember >> That's why it's impossible to break the key, even if we try 255 different binary key for each letter we can have
a lot of readable result without knowing wich is is good one.
"""

"""
Create a list of binary of length n 
Return an object with a representation in hexadecimal
"""
def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range(n)])

"""
Xor each number of keystream with each letter of the message
"""
def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes(key_stream[i] ^ message[i] for i in range(length))


"""
The key must be as long as the message to encrypt all the message
"""
message = "I LOVE YOU"
message = message.encode()
key = generate_key_stream(len(message))
print("Key representation is ", key)
cipher = xor_bytes(key, message)
print(cipher.hex())
print("Cipher message is ",cipher)
"""
To decrypt simply use the same key with the cypher (in bytes representation always)
bytes manage by himself hexadecimal representation or string representation
"""
decryptedMessage = xor_bytes(key, cipher)
print("Decrypted message is ",decryptedMessage)
"""
We can get the key if we have the original message and the cipher (xor property)
"""
k = xor_bytes(message, cipher)
print("The key from message and cipher :", k)
"""
If we try to guess the key with an other message of same length and cipher we get potential fake and good information
"""
guessMessage = "I HATE YOU"
guessMessage = guessMessage.encode()
print(guessMessage.hex())
guessKey = xor_bytes(guessMessage, cipher)
print("The guess key from guess message and cipher :", guessKey)

"""
The guess key is almost good because the guess message is close to the original one
But HATE replace LOVE 
"""
guessDecryptedMessage = xor_bytes(guessKey, cipher)
print("The decrypted message from guess key :", guessDecryptedMessage)

"""
It's useless to try to guess the key from cipher because the key will adapt to decrypt only our message
See file decompose hex message for more INFO 
"""