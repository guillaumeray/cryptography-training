import random

"""
Same function than caesar but instead of using same n decalage, we use random decalage for each letter
pop remove one letter in the list of letter in a random position and return it value
key dictionary is each time different and impredictable
"""
def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters)-1))
    return key

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

"""
Encryption
"""

key = generate_key()
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)

"""
Decryption : 
If we don't know the key but only the algoithm :
    We don't know the number of decalage for each letter because it's random.
    To break the key we have to try 26! = 88^2 = 88 bits security permutation and test the cipher for each one. It's too long
    We know the algorithm but we can not decrypt the cipher without the key.
    An other solution would be to use frequency analysis of the cipher
If we know the key : 
    We can simply reverse the key like caesar cypher
"""

# solution : reverse key dictionary
def get_decryption_key(key):
    dkey={}
    for c in key:
        dkey[key[c]] = c
    return dkey
dkey = get_decryption_key(key)
dMessage = encrypt(dkey, cipher)
print(dMessage)
