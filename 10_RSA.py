import math
import random 

"""
Let's implement RSA in the easy way
RSA is an asymetric cryptography method 
We encrypt with a public key and decrypt with a private key
The couple of public and private key is unique.
How it works ? 
Bob want to send message to Alice
Alice generate the couple of public, private key
Alice send her public key to Bob
Bob can encrypt message with Alice public key
Alice can decrypt message with her private key
"""

def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True

def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p

def lcm(a, b):
    return a*b//math.gcd(a,b)

def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False

def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False

def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n//p

# Step 1: Generate two distinct primes
size = 300
p = get_prime(size)
q = get_prime(size)
while p == q:
    q = get_prime(size)

print("Generate primes :", p, q)

# Step 2 : compute n = p*q
n = p*q
print("Modulus n :", n)

# Step 3 : compute lambda(n) (lcm(n) = lcm(a,b) = a*b/gcd(a,b))
lambda_n = lcm(p-1, q-1)
print("lambda_n:", lambda_n)

# Step 4 : 
e = get_e(lambda_n)
print("Public exponent: ", e)

# Step 5 :
d = get_d(e, lambda_n)
print("Secret exponent: ", d)

# Key generation done 
print("Public key (e,n):", e, n)
print("Secret key (d):", d)

# This is Bob wanting to send a message
# if the message size is more than 123456 then it doest work i do not know why
m = 10
c = m**e % n
print("Bob sends", c)

# This is Alice decrypting the cipher
m = c**d % n
print("Alice decrypt Bob message", m)

# This is Eve
p, q = factor(n)
print("Eve crack factor:", p, q)
print("Eve can now decrypt message")

"""
For the key generation we need : 
p, q : two different primes (keep secret)
n = p * q : modulus
e : exponent
d : modular inverse to e

The public key is 
n : modulus
e : exponent

The private key is 
d : modular

To encrypt message m :
c = m**e % n

To decrypt cipher c :
m = c**d % n

To be true we need this formula to be true : 
(m**e)**d = m**(e*d) = m**1 = m
then e*d = 1 
Not clear for me, need more information on internet

If we can find p and q from n we can find e and d and break RSA

"""