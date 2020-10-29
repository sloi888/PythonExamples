# adapted from https://stackoverflow.com/questions/11747254/python-brute-force-algorithm Martjin Pieters' answer
import random
global guess
length = 5
pasw = ''
characters = 'abcdefghijklmnopqrstuvwxyz'
for i in range(length):
    pasw += characters[random.randint(0, len(characters) - 1)]
chars = 'abcdefghijklmnopqrstuvwxyz' #only limeted myself to lowercase for simplllicity.
base = len(chars)+1
from itertools import chain, product
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

attempts = 0
for attempt in bruteforce(characters, length):
    # match it against your password, or whatever
    print(attempt)
    attempts += 1
    if attempt == pasw:
        break
print(f"Password was {pasw}, took {attempts} attempts")