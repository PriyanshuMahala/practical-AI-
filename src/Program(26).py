#Program to print items in a list

my_list = ["North", "South", "East", "West"]
for i in range(0, len(my_list)):
    if i == len(my_list) - 1:
        print(my_list[i], end=" ")
    else:
        print(my_list[i], end=", ")
