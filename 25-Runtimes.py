from math import sqrt
from sys import stdin


def checkPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i is 0:
            return False
    return True


n = int(input())
for line in stdin:
    val = int(line)
    if (val >= 2 and checkPrime(val)):
        print("Prime")
    else:
        print("Not prime")