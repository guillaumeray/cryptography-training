# The cipher method is just move each letter of a sentence to x+n
# For key 3 YOU become BRX because Y is B and O is R and U is X

""" generate the dictionary key
 n represent the decalage of each letter
 key is the dictionary of original letter with letter + n
 We use modulo % to have the correct decalage no matter big is n and len of letters
 Example :
 we have 26 letter.
    if n is 26 then we will have the same position for each letter
    if n is 27 the we will have a decalage of +1 
"""
def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt+n) % len(letters)]
        cnt+= 1
    return key

"""
Return cipher from a message and a key dictionnary 
If letter is not present in key dictionary we do nothing (like space or special char)
"""
def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

# Generate key dictionary
key = generate_key(3)
# Define message
message = "I LOVE MIGUEL"
# generate cipher msg from key and message
cipher = encrypt(key, message)
print(cipher)

"""
How to decrypt ? 
We have two solutions : 
- Generate a new key dictionary with the same negative key position to get back original letter (need to know n)
- Reverse the key dictionary to get the original letter (need to have the dictionary key only)
"""

# First decrypt solution : move back in the alphabet
# Generate key dictionary with negative number
key = generate_key(-3)
# decrypt the cipher with the new dictionary
decriptCipher = encrypt(key, cipher)
print(decriptCipher)

# Second solution : reverse key dictionary
key = generate_key(3)
def get_decryption_key(key):
    dkey={}
    for c in key:
        dkey[key[c]] = c
    return dkey
dkey = get_decryption_key(key)
dMessage = encrypt(dkey, cipher)
print(dMessage)

"""
Conclusion : 
/!\ If the bad guy know the algorithm to generate the key he can easily break the cipher  
He just has to try 26 different keys dictionary untill getting the good message 
"""

"""
Kerhkhoffs principle:
Eve should not be able to break the cipher even if she knows the cipher (the algorithm)
"""

"""
Example of breaking the cipher knowing the algotithm
"""
print("== BRUTE FORCE ATTACK ==")
for i in range(26):
    dkey = generate_key(i)
    dMessage = encrypt(dkey, cipher)
    print(dMessage)