#program to print odd numbers in a range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for i in range(start, end+1):
    if i % 2 != 0:
        print(i)
