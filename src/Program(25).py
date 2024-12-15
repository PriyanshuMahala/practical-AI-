#program to print prime numbers from 1 to 50

def checkPrime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True


for i in range(0,51):
    if checkPrime(i):
        print(i)