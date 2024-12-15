# Program to print a sorted list

userList = input("Enter elements separated by space: ").split()
userList = [int(item) for item in userList]
userList.sort()

print(userList)
