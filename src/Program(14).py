#Simple error handling in python

while True:
    try:
        _input = int(input("Enter an int: "))
    except ValueError:
        print("Enter a valid integer")
        continue
    break