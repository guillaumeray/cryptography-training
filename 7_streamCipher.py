"""
Stream cipher is the same logic than one time pad
But instead of a random list of number as a key
We use a LCG : une suite qui génère des pseudos nombres aléatoires à partir d'un nombre de base
The main advantage is that from each specific number we have the same following of number.
We generate the key with a seed
"""

class keyStream:
    def __init__(self, key=1):
        self.next = key

    # value of this suite is important to have good randomness
    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next
    
    """
    We have to divide the random by 2**23 and after do modulo 256
    Beceause we need unique result to avoid easy brute force. We 
    must keep the key space of 2**31.
    """
    def get_key_byte(self):
        return (self.rand()//2**23) % 256

def encrypt(key, message):
    return bytes(message[i] ^ key.get_key_byte() for i in range(len(message)))

# generate keyStream with seed 2
key = keyStream(252)
# define and encode message 
message = "HELLO WORLD".encode()
# encrypt message with key stream
cipher = encrypt(key, message)
print(cipher)
# regenerate the keystream to be able to decrypt 
key = keyStream(2)
# decrypt from keystream and cipher
decryptMessage = encrypt(key, cipher)
print(decryptMessage)


"""
One of the big advantage of stream cipher is that even
if we lost one or several bit during the transmission of cipher
we can still decode part of the message.
"""
"""
The big default of strem cipher is lack of authenticity
If attacker know part of the message, he can change it 
Example below
"""

"""
! Important pour comprendre propriétés de XOR !
ord('S') = 83
key[0] = 19
XOR peut être vu comme une soustraction dans des cas particuliers
Exemple les deux premières lettres chiffrées
ord('S') ^ key[0] = 83 ^ 19 = 83 - 19 = 64
Pour déchiffrer on utilise les mêmes clés
64^19 = 64 + 19 = 83
Pour mieux comprendre on peut voir le XOR comme un soustracteur c'est
pour cela qu'on peut chiffrer en soustrayant une clé et déchiffrer en l'ajoutant pour retrouver le nbr d'origine.
Mais ce n'est pas toujours le cas (!)

Si on veut changer la lettre S en A 
1ère solution : 
On peut retrouver la clé car on connait la lettre chiffrée et la lettre claire
key[0] = 64 ^ ord('S') = 64 ^ 83 = 19
On peut utiliser ensuite la clé pour chiffré A : ord('A') ^ 19 = 65 ^ 19 = 82

2ème solution : 
ord('S)^ord('A') ^ ord('S)^key[0] = 83^65 ^ 83^19 = 65 ^ 19 = 18 ^ 63 = 82 
Grâce à la propriété de xor a^b^a^c = b^c
On a chiffré la lettre A avec la clé 19 sans connaître la clé !
Mais juste en connaissant A et la lettre chiffré
"""

print("Chiffré A avec la clé : ord('S')^ord('A')^ord('S')^19 : ", ord('S')^ord('A')^ord('S')^19)
print("Déchiffré A avec la clé : 82 ^ 19 : ", 82^19)
print("65 is ord('A')")


"""
Example of stream CIPHER attack 
We want to transform message 'SEND 10$' to 'SEND 90$'
We use 0 as filter because 0^10 = 10 (true for any number 0 ^ x = x)
If we know the position of the letter to change we can change it
"""
def modification(cipher):
    mod = [0]*len(cipher)
    mod[5] = ord('1') ^ ord('9') # replace 1 to 9
    return bytes(mod[i] ^ cipher[i] for i in range(len(cipher)))

key = keyStream(2)
message = "SEND 10$".encode()
cipher = encrypt(key, message)
# ATTACK ! interception and modification of cipher
cipher = modification(cipher)
key = keyStream(2)
decryptMessage = encrypt(key, cipher)
print(decryptMessage)

"""
Conclusion : 
First weakness : Need authenticity
It's possible to intercept and hack encrypted message with stream cipher
That's why we need AUTHENTICITY to be sure we get the cipher from the good person

Second weakness : Exploiting re-use of key
If Eve send a text to Alice and Alice send it to Bob
Then Eve can intercept cipher message and get the key from the plain text
If Alice reuse the same key Eve will be able to decrypt all messages bewteen Alice and Bob

Third weakness : Entropy 
When we can easily brute force the key if we know a part of a message like the header.
See below example
"""

"""
Brute force a key space of 2**31 is easy
Guess the key stream from header and cipher
key = text ^ cipher
"""
def brute_force(plain, cipher):
    for k in range(2**31):
        bf_key= keyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
        else:
            return k
    return false

# This is Alice
secret_key = 678 
key = keyStream(secret_key)
header = "MESSAGE: "
message = (header + "My secret message").encode()
cipher = encrypt(key, message)
print(cipher)

# This is Bob
key = keyStream(secret_key)
message = encrypt(key, cipher)
print(message)

# This is Eve
# Eve can bruteforce key thanks to the header and the cipher
bf_key = brute_force(header.encode(), cipher)
print("Eve brute force key ", bf_key)
key = keyStream(bf_key)
message = encrypt(key, cipher)
print(message)