import math
import random 

"""
About KEY EXCHANGE
"""

"""
@p : entier 
math.isqrt(p) : renvoie la racine carré de p (arrondi décimale inférieur pour carré non parfait)
return true si premier
return false si non premier

Un nombre premier est un nombre entier >= 2 divisible par 1 et lui même uniquement
Pour découvrir si un nombre est premier on peut chercher tous ses diviseurs possible
entre 2 et p. 
Si p % i == 0 c'est qu'on a découvert un diviseur de p DONC p n'est pas premier
Sinon p est forcément premier.
Pour optimiser l'algo et la mémoire on réduit la recherche jusqu'à racine carré de p.
En effet si p est non premier, son carré renverra un de ses 1er diviseur, il sera inutile de chercher au dela.
Exemple : 
pour p = 100, sa racine est 10 
100 % 10 == 0, pas besoin d'aller plus loin
le premier diviseur de 100 sera 2
CQFD = Les diviseur vont par pair l'un se trouve de 2 à racine(p) et l'autre de racine(p) à n
"""
def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True

"""
size: taille de la zone de recherche 
return prime number
"""
def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p
"""
g: int, generator to check
p: int, prime number

Pour ttes les valeurs i de 1 à p-1 on check que le generateur (g**i % p) 
ne retourne pas la valeur 1. On veut check si le générateur est fiable.
Si l'ensemble des calculs ne retourne pas 1 c'est un bon générateur.
"""
def is_generator(g, p):
    for i in range(1, p - 1):
        calcul = (g**i) % p
        #print("{}**{} % {} = {}".format(g, i, p, calcul))
        if calcul == 1:
            #print("not a good generator, next one")
            return False
    # loop is finish, no calcul return 1 then it's a good generator
    return True

"""
p: int, prime number

D'après la valeur p on souhaite trouver le générateur g
"""
def get_generator(p):
    for g in range(2, p):
        if is_generator(g, p):
            return g

# Public information (generator and prime number)
p = get_prime(1234)
print("prime is ", p)
g = get_generator(p)
print(g, p)

# Alice
# a is Alice private key
a = random.randrange(0, p)
g_a = (g**a) % p
print("Alice private key :", a)
print("Alice public key :", g_a)

# Bobb
# b is Bob private key
b = random.randrange(0, p)
g_b = (g**b) % p
print("Bob private key :", b)
print("Bob public key :", g_b)

# Alice get bob public key and calculate common key
g_ab = (g_b**a) % p
# Bob get Alice public key and calculate common key
g_ba = (g_a**b) % p 
print("Common key of Alice {} and Bob {}".format(g_ab, g_ba))

"""
Even if Eve know the prime number, the generator and public key of 
Bob and Alice she can not find the common key for Alice and Bob.
This secuity is guarantee thanks to math problem of discrete logarithm.
We can then safely distribute symetric key for encryption exchange (stream or block cipher)
"""

