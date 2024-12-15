#check if a number is prime


def checkPrime(n ):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True


print(checkPrime(35797))
print(checkPrime(27))