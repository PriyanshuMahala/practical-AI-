import random

#Generate a random number between a range

Starting_Num = int(input("Enter the lowest possibility: "))
Ending_Num = int(input("Enter the highest possibility: "))

try:
    random_num = random.randrange(Starting_Num, Ending_Num)
    print(random_num)
except ValueError:
    print("Enter a valid range with a difference of at least one")


