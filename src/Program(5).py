#factorial function using recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"3! = {factorial(3)}")
