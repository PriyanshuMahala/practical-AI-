#Calculate volume of sphere from 4/3 * PIr3

PI = 3.1415926535
r = int(input("Enter the radius of the sphere: "))
volume = (4/3) * PI * (r**3)
print("Volume of sphere with radius", r,"=", volume, "units^3")
