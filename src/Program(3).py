#calculator
while True:
    print("+, -, *, /, (e)xit")
    operation = input("Enter: ").lower()

    if operation not in {'+', '-', '*', '/', 'e'}:
        print("Invalid input!")
        continue

    if operation == 'e':
        print("Exiting")
        break

    try:
        num1 = int(input("Enter #1: "))
        num2 = int(input("Enter #2: "))

        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 == 0:
                print("Cannot divide by 0")
                continue
            print(f"{num1} / {num2} = {num1 / num2}")

    except ValueError:
        print("Invalid input. Please enter a integer next time.")

